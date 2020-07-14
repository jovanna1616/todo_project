"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

app_name = "todos"

urlpatterns = [
    path("todos/", views.todos, name="todos"),
    path("todos/create", views.todo_create_form, name = "todo-create-form"),
    path("todos/create-request", views.todo_create_request, name="todo-create-request"),
    path("todos/<int:todo_id>/", views.todo, name="todo"),
    path("todos/<int:todo_id>/update/", views.todo_update_form, name="todo-update-form"),
    path("todos/<int:todo_id>/update-request/", views.todo_update_request, name="todo-update-request"),
    path("todos/<int:todo_id>/delete/", views.todo_delete, name="todo-delete"),
]
