from django.shortcuts import render

# Create your views here.

# customer 
def customerHome(request):
    return render(request, "customer/home.html")

def formBorrowBook(request):
    return render(request, "customer/form-borrow.html")

def customerHistory(request):
    return render(request, "customer/history.html")