from django.urls import path
from customer import views

urlpatterns = [
    path("customer-dashboard/", views.customerDashboard, name="customer-dashboard"),
    path("list-of-book/", views.listOfBook, name="list-of-book"),
    path("history/", views.history, name="history"),
]
