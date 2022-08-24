from re import template
from django.shortcuts import render, HttpResponse


# Create your views here.

def dashboard_index(request):
    return render(request,'dashboard/index.html')

