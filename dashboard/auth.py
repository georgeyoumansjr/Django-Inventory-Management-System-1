from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect


def admin_only(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_staff:
            return view_function(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/dashboard')
    return wrapper_function
