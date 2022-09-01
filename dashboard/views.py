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
            return redirect('/dashboard/')
        else:
            print("FORM ERROR")

    context = {
        'form' : form,
        'title':'Add Products',
        }

    return render(request,'dashboard/add_product.html',context=context)






def search_available_products(request):
    form = SearchForm()

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