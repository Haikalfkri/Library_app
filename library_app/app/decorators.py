from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        # check if the user is authenticated
        if request.user.is_authenticated:
            # check the role == 'admin
            if request.user.role == 'admin':
                return redirect('admin-home')
            
            # check the role == 'user
            if request.user.role == 'user':
                return redirect('customer-home') 
        else:
            # return current view
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


def allowed_users(allowed_users=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                # get the name of the group
                group = request.user.groups.all()[0].name
                
            # check if the group in allowed_user
            if group in allowed_users:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to view this page')
            
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
            
        group = None
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
        if group == 'user':
            return redirect('customer-home')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
    return wrapper_func