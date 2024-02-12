from django.shortcuts import render

# Create your views here.

# customer 
def customerHome(request):
    return render(request, "customer/home.html")

def formBorrowBook(request):
    return render(request, "customer/form-borrow.html")

def customerHistory(request):
    return render(request, "customer/history.html")

def borrowingForm(request):
    return render(request, "customer/form-borrow.html")


# admin
def adminHome(request):
    return render(request, "library_admin/manage-book.html")

def borrowHistory(request):
    return render(request, "library_admin/history.html")

def listOfUser(request):
    return render(request, "library_admin/list-of-user.html")

def addBook(request):
    return render(request, "library_admin/add-book.html")

def addAdmin(request):
    return render(request, "library_admin/add-admin.html")