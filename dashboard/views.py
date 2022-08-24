from django.shortcuts import render, HttpResponse


# Create your views here.

def dashboard_index(request):
    return render(request,'dashboard/index.html')

def add_products(request):
    return HttpResponse("add_products PAGE")

def search_available_products(request):
    return HttpResponse("search_available_products PAGE")

def view_available_products(request):
    return HttpResponse("view_available_products PAGE")

def sell_available_products(request):
    return HttpResponse("sell_available_products PAGE")

def view_sold_products(request):
    return HttpResponse("view_sold_products PAGE")

def users(request):
    return HttpResponse("users PAGE")