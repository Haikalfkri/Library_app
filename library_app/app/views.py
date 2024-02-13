from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from app.forms import AdminRegisterForm


# Create your views here.

# customer 
login_required(login_url='login')
def customerHome(request):
    return render(request, "customer/home.html")


login_required(login_url='login')
def formBorrowBook(request):
    return render(request, "customer/form-borrow.html")


login_required(login_url='login')
def customerHistory(request):
    return render(request, "customer/history.html")


login_required(login_url='login')
def borrowingForm(request):
    return render(request, "customer/form-borrow.html")



# admin
login_required(login_url='login')
def adminHome(request):
    return render(request, "library_admin/manage-book.html")


login_required(login_url='login')
def borrowHistory(request):
    return render(request, "library_admin/history.html")


login_required(login_url='login')
def listOfUser(request):
    return render(request, "library_admin/list-of-user.html")


login_required(login_url='login')
def addBook(request):
    return render(request, "library_admin/add-book.html")


login_required(login_url='login')
def addAdmin(request):
    if request.method == "POST":
        form = AdminRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            group = Group.objects.get(name="admin")
            user.groups.add(group)
            
            messages.success(request, "Register For Admin Succesfully")
            return redirect('add-admin')
        else:
            messages.error(request, "Invalid Register")
    else:
        form = AdminRegisterForm()
                    
    return render(request, "library_admin/add-admin.html", {'form': form})