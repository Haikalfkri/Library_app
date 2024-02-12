from django.shortcuts import render

# Create your views here.

# customer 
def customerHome(request):
    return render(request, "customer/home.html")

def formBorrowBook(request):
    return render(request, "customer/form-borrow.html")

def customerHistory(request):
    return render(request, "customer/history.html")


# admin
def adminHome(request):
    return render(request, "library_admin/home.html")

def borrowHistory(request):
    return render(request, "library_admin/history.html")