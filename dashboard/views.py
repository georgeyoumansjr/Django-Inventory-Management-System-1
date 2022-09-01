from django.shortcuts import render, HttpResponse
from . import models
from .addforms import AddProductForm

# Create your views here.

def dashboard_index(request):
    return render(request,'dashboard/index.html',context={'title':'Dashboard'})




    
#add_products
def add_products(request):
    form = AddProductForm()

    if request.method == 'POST':
        form = AddProductForm(request.POST)
        
        if form.is_valid():
            print()
            print(form.cleaned_data)
            print(
                form.cleaned_data['product_name'], 
                form.cleaned_data['product_price'], 
                form.cleaned_data['product_quantity']
            )

    context = {
        'form' : form,
        'title':'Add Products',
        }

    return render(request,'dashboard/add_product.html',context=context)



def search_available_products(request):
    return HttpResponse("search_available_products PAGE")

# view_available_products 
def view_available_products(request):

    all_products = models.Available_product_table.objects.all()
    context = {
        'all_products' : all_products,
        'title' : 'All Products',
        }
            
    return render(request,'dashboard/view_available_products.html',context=context)


def sell_available_products(request):
    return HttpResponse("sell_available_products PAGE")


# view_sold_products
def view_sold_products(request):
    # --- link sold_products_table
    all_products = models.Available_product_table.objects.all()
    context = {
        'all_products' : all_products,
        'title' : 'Sold Products',
        }
            
    return render(request,'dashboard/view_sold_products.html',context=context)


def users(request):
    return HttpResponse("users PAGE")