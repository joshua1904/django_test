from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.get_quiz, name="get_quiz")
]