from django.shortcuts import render, HttpResponse, redirect
from . import models
from .forms import AddProductForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .auth import admin_only
from django.contrib.auth.models import User
from django.db.models import Q
from django.core import mail

connection = mail.get_connection()

connection.open()


@login_required
def dashboard_index(request):   
    shop_name = request.user.username
    shop_name = shop_name.split("_")
    shop_name = map(lambda x: x.capitalize(),shop_name)
    shop_name = ' '.join(shop_name)

    return render(request,'dashboard/index.html',context={'title':'Dashboard',"shop":str(shop_name),"user": request.user})



#add_products
@login_required
def add_products(request):
    form = AddProductForm()

    if request.method == 'POST':
        form = AddProductForm(request.POST)
        user = request.user
        
        if form.is_valid():
            created = models.Available_product_table.objects.create(added_by=request.user,**form.cleaned_data)
            # form.save()
            
            context = {
                'result' : 'New Product Added successfully',
                'title':'Add Products',
            }
            return render(request,'dashboard/result.html',context=context)

        else:
            context = {
                'result' : 'ERROR',
                'title':'Add Products',
            }
            return render(request,'dashboard/result.html',context=context)

    context = {
        'form' : form,
        'title':'Add Products',
        }

    return render(request,'dashboard/add_product.html',context=context)





# search_available_products
@login_required
def search_available_products(request):
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            search_product = form.cleaned_data['search_product']
            
            all_products = models.Available_product_table.objects.filter(product_name = search_product).values()  
            #print(all_products)
            context = {
                'all_products' : all_products,
                'title' : 'Search Result',
            }
            
            return render(request,'dashboard/view_available_products.html',context=context)


    context = {
        'form' : form,
        'title':'Search Products',
        }

    return render(request,'dashboard/search_product.html',context=context)


# view_available_products 
@login_required
def view_available_products(request):
    if request.user.is_superuser:
        all_products = models.Available_product_table.objects.all()
        
        context = {
            'all_products' : all_products,
            'title' : 'All Products',
            }
            
        return render(request,'dashboard/view_available_products.html',context=context)
    else:
        all_products = models.Available_product_table.objects.filter(added_by=request.user)
        context = {
            'all_products' : all_products,
            'title' : 'All Products',
            }
            
        return render(request,'dashboard/view_available_products.html',context=context)

from datetime import datetime
# from django.utils.timezone import get_current_timezone
@admin_only
@login_required
def view_availableUsers(request):
    all_users = User.objects.only("id","username","date_joined").filter(~Q(is_superuser=1))
    
    for user in all_users:
        shop_name = user.username
        shop_name = shop_name.split("_")
        shop_name = map(lambda x: x.capitalize(),shop_name)
        shop_name = ' '.join(shop_name)
        # tz = get_current_timezone()
        dt = user.date_joined.strftime('%m/%d/%Y')
        user.shop_name  = shop_name
        user.date_joined = dt
    print(all_users)
    context = {
        "users" : all_users
    }

    return render(request,"dashboard/view_available_shops.html",context= context)


@login_required
def userDetail(request,pk):
    user_detail = User.objects.get(id=pk)
    shop_name = user_detail.username
    shop_name = shop_name.split("_")
    shop_name = map(lambda x: x.capitalize(),shop_name)
    shop_name = ' '.join(shop_name)

    listed_products = models.Available_product_table.objects.filter(added_by=pk)
    sold_products = models.Sold_product_table.objects.filter(sold_by=pk)
    context = {
        "shop": shop_name,
        "listings": listed_products,
        "sold": sold_products
    }
    return render(request,"dashboard/user_detail.html",context= context)


# sell_available_products
@login_required
def sell_available_products(request):

    if request.method == 'POST':
        sell_product_id = request.POST['product_id']
        sell_qty = int(request.POST['sellqty'])
        
        sell_product = models.Available_product_table.objects.filter(id = sell_product_id).values()
        sell_product = sell_product[0]

        if  sell_qty <= sell_product['product_quantity']:
            user = request.user
            product = models.Sold_product_table(
                product_id = sell_product['id'], 
                product_name = sell_product['product_name'],
                product_price = sell_product['product_price'],
                product_quantity = sell_qty,
                sold_by = user
            )
            product.save()

            # UPDATE Available_product_table
            remaning_qty = sell_product['product_quantity'] - sell_qty

            update_product = models.Available_product_table.objects.get(id = sell_product_id)
            update_product.product_quantity = remaning_qty
            update_product.save()
            
            subject = sell_qty + " of "+ sell_product['product_name'] + " Sold"

            email = EmailMessage(subject, 'Body', to=['coyim41998@ezgiant.com'])
            
            email.send()
            
            context = {
                'result' : 'Product sold successfully!',
                'title':'Sell Products',
            }
            return render(request,'dashboard/result.html',context=context)

        else:
            context = {
                'result' : 'Enter Quantity is less than available stock or Product is Out of Stock!',
                'title':'Sell Products',
            }
            return render(request,'dashboard/result.html',context=context)
        
    if request.user.is_superuser:
        all_products = models.Available_product_table.objects.all()
        context = {
            'all_products' : all_products,
            'title' : 'Sell Products',
            }
                
        return render(request,'dashboard/sell_products.html',context=context)
    else:
        all_products = models.Available_product_table.objects.filter(added_by=request.user)
        context = {
            'all_products' : all_products,
            'title' : 'Sell Products',
            }
                
        return render(request,'dashboard/sell_products.html',context=context)





# view_sold_products
@login_required
def view_sold_products(request):
    if request.user.is_superuser:
        all_sold_products = models.Sold_product_table.objects.all()
        context = {
            'all_sold_products' : all_sold_products,
            'title' : 'Sold Products',
            }
                
        return render(request,'dashboard/view_sold_products.html',context=context)
    else:
        all_sold_products = models.Sold_product_table.objects.filter(sold_by=request.user)
        context = {
            'all_sold_products' : all_sold_products,
            'title' : 'Sold Products',
            }
                
        return render(request,'dashboard/view_sold_products.html',context=context)





@admin_only
@login_required
def users(request):
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        
        if form.is_valid():
            form.save()
            
            context = {
                'result' : 'User Added successfully',
                'title':'Add User',
            }
            return render(request,'dashboard/result.html',context=context)

        else:
            context = {
                'result' : 'ERROR - Does not meet the requirements!',
                'title':'Add User',
            }
            return render(request,'dashboard/result.html',context=context)

    context = {
        'form' : form,
        'title':'Add User',
        }

    return render(request,'dashboard/user.html',context=context)
