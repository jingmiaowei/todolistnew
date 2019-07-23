from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.TodoListView, name = 'home'),
    path('add/', views.TodoAdd,name='add'),
    path('delete/<Todolist_id>/', views.TodoDelete,name='delete'),
    path('edit/', views.TodoEdit,name= 'edit'),
    path('newedit/<Todolist_id>/', views.NewEdit,name='newedit'),
    path('finish/<Todolist_id>/', views.Finish,name='finish'),
]