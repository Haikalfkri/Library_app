from django.urls import path
from . import views

urlpatterns = [
    path("customer-home/", views.customerHome, name="customer-home"),
    path("form-borrow-book/", views.formBorrowBook, name="form-borrow-book"),
    path("customer-history/", views.customerHistory, name="customer-history"),
    
    path("admin-home/", views.adminHome, name="admin-home"),
    path("admin-history/", views.borrowHistory, name="admin-history"),
]
