from django.shortcuts import render

# Create your views here.
def customerDashboard(request):
    return render(request, "customer/customer-dashboard.html")

def listOfBook(request):
    return render(request, "customer/book.html")

def history(request):
    return render(request, "customer/history.html")