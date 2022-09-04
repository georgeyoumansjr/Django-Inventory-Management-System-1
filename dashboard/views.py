from django.shortcuts import render, HttpResponse, redirect
from . import models
from .forms import AddProductForm, SearchForm


# Create your views here.

def dashboard_index(request):
    return render(request,'dashboard/index.html',context={'title':'Dashboard'})




    
#add_products
def add_products(request):
    form = AddProductForm()

    if request.method == 'POST':
        form = AddProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            
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
def view_available_products(request):

    all_products = models.Available_product_table.objects.all()
    context = {
        'all_products' : all_products,
        'title' : 'All Products',
        }
            
    return render(request,'dashboard/view_available_products.html',context=context)





# sell_available_products
def sell_available_products(request):

    if request.method == 'POST':
        sell_product_id = request.POST['product_id']
        sell_qty = int(request.POST['sellqty'])
        
        sell_product = models.Available_product_table.objects.filter(id = sell_product_id).values()
        sell_product = sell_product[0]

        if  sell_qty <= sell_product['product_quantity']:
            product = models.Sold_product_table(
                product_id = sell_product['id'], 
                product_name = sell_product['product_name'],
                product_price = sell_product['product_price'],
                product_quantity = sell_qty,
            )
            product.save()

            # UPDATE Available_product_table
            remaning_qty = sell_product['product_quantity'] - sell_qty

            update_product = models.Available_product_table.objects.get(id = sell_product_id)
            update_product.product_quantity = remaning_qty
            update_product.save()
            

        else:
            test = 'FALSE'
        

    all_products = models.Available_product_table.objects.all()
    context = {
        'all_products' : all_products,
        'title' : 'Sell Products',
        't1' : 'test',
        }
            
    return render(request,'dashboard/sell_products.html',context=context)






# view_sold_products
def view_sold_products(request):
    all_sold_products = models.Sold_product_table.objects.all()
    context = {
        'all_sold_products' : all_sold_products,
        'title' : 'Sold Products',
        }
            
    return render(request,'dashboard/view_sold_products.html',context=context)






def users(request):
    return HttpResponse("users PAGE")