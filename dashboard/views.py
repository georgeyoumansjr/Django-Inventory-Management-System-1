from django.shortcuts import render, HttpResponse, redirect
from . import models
from .forms import AddProductForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .auth import admin_only

# Create your views here.

@login_required
def dashboard_index(request):
    return render(request,'dashboard/index.html',context={'title':'Dashboard'})




    
#add_products
@login_required
def add_products(request):
    form = AddProductForm()

    if request.method == 'POST':
        form = AddProductForm(request.POST)
        user = request.user
        
        if form.is_valid():
            created = Playlist.objects.create(added_by=request.user,**form.cleaned_data)
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
        

    all_products = models.Available_product_table.objects.all()
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
