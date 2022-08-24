from re import template
from django.shortcuts import render, HttpResponse


# Create your views here.

def dashboard(request):
    return render(request,'dashboard/index.html')
