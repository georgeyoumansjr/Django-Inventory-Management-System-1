from multiprocessing import context
from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def dashboard_index(request):
    return render(request,'dashboard/index.html')

def add_products(request):
    return HttpResponse("add_products PAGE")

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

def view_sold_products(request):
    return HttpResponse("view_sold_products PAGE")

def users(request):
    return HttpResponse("users PAGE")