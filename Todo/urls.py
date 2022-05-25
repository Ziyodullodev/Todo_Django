from django.urls import path
from .views import *
urlpatterns = [
    path('', TodoView, name="home"),
    path('update/<str:pk>', UpdateTodoView, name="update-Todo"),
    path('delete/<int:pk>', DeleteTodoView, name="delete-Todo"),
    path('test/', Test, name="Test"),
]