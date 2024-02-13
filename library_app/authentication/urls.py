from django.urls import path
from authentication import views

urlpatterns = [
    path("login/", views.UserLogin, name="login"),
    path("register/", views.UserRegister, name="register"),
]
