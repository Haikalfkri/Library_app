from django.urls import path
from . import views

urlpatterns = [
    # urls for customer
    path("customer-home/", views.customerHome, name="customer-home"),
    path("customer-history/", views.customerHistory, name="customer-history"),
    path("borrowing-form/<int:id>/", views.borrowingForm, name="borrowing-form"),
    
    # urls for library admin
    path("admin-home/", views.adminHome, name="admin-home"),
    path("admin-history/", views.borrowHistory, name="admin-history"),
    path("add-admin/", views.addAdmin, name="add-admin"),
    
    path("list-of-user/", views.listOfUser, name="list-of-user"),
    path("delete-user/<int:pk>/", views.deleteUser, name="delete-user"),
    path("update-user/<int:pk>/", views.editUser, name="update-user"),
    
    path("add-book/", views.addBook, name="add-book"),
    path("delete-book/<int:pk>/", views.deleteBook, name="delete-book"),
    path("update-book/<int:pk>/", views.editBook, name="update-book"),
]
