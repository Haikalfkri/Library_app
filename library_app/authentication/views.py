from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# to check the role and group 
@login_required(login_url='login')
def redirect_based_on_role_and_group(request):
    user = request.user

    if user.role == "admin" and user.groups.filter(name='admin').exists():
                return redirect('admin-home')
    elif user.role == "user" and user.groups.filter(name='user').exists():
                return redirect('customer-home')
    else:
        messages.error(request, "You dont have any permission")
        return redirect('login')


def UserLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect_based_on_role_and_group(request)  
        else:
            messages.error(request, 'Username OR password is incorrect')
    
    return render(request, "authentication/login.html")


def UserRegister(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()   
            
            group = Group.objects.get(name='user')
            user.groups.add(group)
                 
            messages.success(request, "Register Successfully")
            return redirect('login')
        else:
            messages.error(request, "Invalid Register")
    else:
        form = UserRegistrationForm()
    
    return render(request, "authentication/register.html", {'form': form})


def UserLogout(request):
    logout(request)
    messages.success(request, "Logout Succesfully")
    return redirect('login')