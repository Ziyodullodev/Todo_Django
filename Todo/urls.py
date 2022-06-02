from django.urls import path
from .views import *
urlpatterns = [
    path('', TodoView, name="home"),
    path('<str:pk>', UpdateTodoView, name="edit-task"),
    path('end/<str:pk>', StartTask, name="end-task"),
    path('start/<str:pk>', ComplatedTask, name="start-task"),
    path('del/<int:pk>', DeleteTodoView, name="delete-Todo"),
    # path('test/', Test, name="Test"),
]