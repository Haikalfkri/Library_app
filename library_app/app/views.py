from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.decorators import allowed_users, admin_only
from django.contrib.auth.models import Group
from django.db.models import Q

from app.forms import AdminRegisterForm, AddBookForm, BorrowBookForm
from app.models import BookModel, CustomUser, BorrowBookModel

from django.utils import timezone

# Create your views here.

# customer 
@login_required(login_url='login')
@allowed_users(allowed_users=['user'])
def customerHome(request):
    books = BookModel.objects.all().order_by('id')

    # Get a set of book IDs that the user has currently borrowed
    borrowed_books_ids = set(BorrowBookModel.objects.filter(
        user=request.user
    ).values_list('book_id', flat=True))

    # Get a set of book IDs that the user has borrowed and not yet returned
    not_returned_books_ids = set(BorrowBookModel.objects.filter(
        user=request.user,
        date_return__gt=timezone.now()
    ).values_list('book_id', flat=True))

    context = {
        'books': books,
        'borrowed_books_ids': borrowed_books_ids,
        'not_returned_books_ids': not_returned_books_ids,
    }

    return render(request, "customer/home.html", context)



@login_required(login_url='login')
@allowed_users(allowed_users=['user'])
def customerHistory(request):
    current_user = request.user
    customer_history = BorrowBookModel.objects.filter(user=current_user)

    context = {
        'histories': customer_history,
    }
    
    return render(request, "customer/history.html", context)



@login_required(login_url='login')
@allowed_users(allowed_users=['user'])
def borrowingForm(request, id):
    book = BookModel.objects.get(id=id)
    current_user = request.user
    
    if request.method == "POST":
        form = BorrowBookForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Set the current user and book id to the form
            form.instance.user = current_user
            form.instance.book = book
            
            form.save()
            messages.success(request, "Borrow Book Successfully")
            return redirect('customer-home')
        else:
            messages.error(request, "Failed to Borrow")
            print(form.errors)
    else:
        form = BorrowBookForm(initial={'books': [book]})
    return render(request, "customer/form-borrow.html", {'form': form})




# admin
# function for showing list of book
@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
def adminHome(request):
    book_list = BookModel.objects.all().order_by('id')
    
    # search functionality
    book_search = request.GET.get('search')
    if book_search:
        # For search by title and author
        book_list = book_list.filter(Q(title__icontains=book_search) | Q(author__icontains=book_search))
    
    context = {
        'books': book_list,
    }
    
    return render(request, "library_admin/manage-book.html", context)



# function for adding book to the database
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



# function for delete book from database
@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
def deleteBook(request, pk):
    book = BookModel.objects.get(pk=pk)
    book.delete()
    messages.success(request, "Book Succesfully Deleted")
    return redirect('admin-home')



# function for update or edit book data
@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
def editBook(request, pk):
    book = BookModel.objects.get(pk=pk)

    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES, instance=book)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Update Succesfull")
            return redirect("admin-home")
        else:
            messages.error(request, "Failed to Update Data")
    else:
        form = AddBookForm(instance=book)
        
    return render(request, "library_admin/edit-book.html", {'form': form})



# for showing history who borrowing the book
@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
def borrowHistory(request):
    borrow_history = BorrowBookModel.objects.all()
    
    context = {
        'borrow_histories': borrow_history,
    }
    
    return render(request, "library_admin/history.html", context)



# for showing list of user
@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
def listOfUser(request):
    users = CustomUser.objects.all().order_by('id')
    
    context = {
        'users': users
    }
    
    return render(request, "library_admin/list-of-user.html", context)


# function for delete the user 
@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
def deleteUser(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user.delete()
    messages.success(request, "User Successfully Deleted")
    return redirect('list-of-user')



# function for editing the data of the user
@login_required(login_url='login')
@admin_only
@allowed_users(allowed_users=['admin'])
def editUser(request, pk):
    user = CustomUser.objects.get(pk=pk)
    
    if request.method == "POST":
        # Exclude role for exclude role from the forms and setup to from default role is user to role admin
        form = AdminRegisterForm(request.POST, instance=user, exclude=['role'])
        
        if form.is_valid():
            form.save()
            messages.success(request, "Success Updating User")
            return redirect("list-of-user")
        else:
            messages.error(request, "Failed to Update Data")
            # print(form.errors)
    else:
        form = AdminRegisterForm(instance=user)
    
    return render(request, "library_admin/edit-user.html", {'form': form})



# function for adding the user
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
            return redirect('list-of-user')
        else:
            messages.error(request, "Invalid Register")
    else:
        form = AdminRegisterForm()
                    
    return render(request, "library_admin/add-admin.html", {'form': form})