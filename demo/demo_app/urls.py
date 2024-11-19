from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.ShoppingList.as_view(), name="TODO list"),
    path("list/<int:pk>", views.ShoppingDetailView.as_view(), name="Hallo"),
    path("add-shopping/", views.add_shopping_form, name="add_shopping"),
    path("add-item/<int:pk>", views.add_item_form, name = "add Item"),
    path("delete-shopping/<int:pk>", views.DeleteShopping.as_view(), name="delete-shopping"),
    path("delete-item/<int:item_pk>/<int:shopping_pk>", views.delete_item, name="delete-item")

]