from django.urls import path
from .views import todo_list, todo_detail, create_todo, delete_todo

urlpatterns = [
    path('todos/', todo_list, name='todo_list'),
    path('todos/<int:todo_id>/', todo_detail, name='todo_detail'),
    path('todos/add/', create_todo, name='create_todo'),
    path('todos/<int:todo_id>/delete/', delete_todo, name='delete_todo'),
]
