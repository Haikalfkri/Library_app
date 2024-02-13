from django.shortcuts import render

# Create your views here.
def UserLogin(request):
    return render(request, "authentication/login.html")

def UserRegister(request):
    return render(request, "authentication/register.html")