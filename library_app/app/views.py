from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.decorators import allowed_users, admin_only
from django.contrib.auth.models import Group
from django.db.models import Q

from app.forms import AdminRegisterForm, AddBookForm
from app.models import BookModel

# Create your views here.

# customer 
@login_required(login_url='login')
@allowed_users(allowed_users=['user'])
def customerHome(request):
    return render(request, "customer/home.html")


@login_required(login_url='login')
@allowed_users(allowed_users=['user'])
def formBorrowBook(request):
    return render(request, "customer/form-borrow.html")


@login_required(login_url='login')
@allowed_users(allowed_users=['user'])
def customerHistory(request):
    return render(request, "customer/history.html")


@login_required(login_url='login')
@allowed_users(allowed_users=['user'])
def borrowingForm(request):
    return render(request, "customer/form-borrow.html")



# admin
@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
def adminHome(request):
    book_list = BookModel.objects.all()
    
    # search functionality
    book_search = request.GET.get('search')
    if book_search:
        book_list = book_list.filter(Q(title__icontains=book_search) | Q(author__icontains=book_search))
    
    context = {
        'books': book_list,
    }
    
    return render(request, "library_admin/manage-book.html", context)


@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
def borrowHistory(request):
    return render(request, "library_admin/history.html")


@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
def listOfUser(request):
    return render(request, "library_admin/list-of-user.html")


@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
def addBook(request):
    if request.method == "POST":
        # print(request.POST)
        # print(request.FILES)
        
        form = AddBookForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Book Successfully Added")
            return redirect('add-book')
    else:
        form = AddBookForm()
    
    return render(request, "library_admin/add-book.html", {'form': form})


@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
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