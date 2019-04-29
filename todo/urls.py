from django.urls import path
from todo import views as todo

urlpatterns = [
    path('login-success/', todo.login_success, name="login_success"),
    path('create-todo/', todo.create_todo, name="create_todo"),
    path('edit-todo/<int:id>/', todo.edit_todo, name="edit_todo"),
    path('delete-todo/<int:id>/', todo.delete_todo, name="delete_todo"),
]