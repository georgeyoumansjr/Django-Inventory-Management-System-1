from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def dashboard_index(request):
    return render(request,'dashboard/index.html',context={'title':'Dashboard'})


def add_products(request):
      return render(request,'dashboard/test.html',context={'title':'TEST'})


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