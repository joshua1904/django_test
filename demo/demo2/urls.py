from django.urls import path, include
from .views import QuoteList, AddQuote, add_person, DeleteQuote

urlpatterns = [
    path("", QuoteList.as_view(), name="quote_list"),
    path("add-quote/", AddQuote.as_view(), name="add_quote"),
    path("add-person/", add_person, name="add_person"),
    path("delete-quote/<int:pk>", DeleteQuote.as_view(), name="delete_quote")

]