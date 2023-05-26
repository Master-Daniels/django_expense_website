from django.urls import path
from . import views

urlpatterns = [
    path("expenses/", views.index, name="index"),
    path("add-expense/", views.add_expense, name="add_expense")
]
