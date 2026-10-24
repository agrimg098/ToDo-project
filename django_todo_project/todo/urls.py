from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.todo_list, name="list"),
    path("<int:task_id>/edit/", views.edit_task, name="edit"),
    path("<int:task_id>/toggle/", views.toggle_task, name="toggle"),
    path("<int:task_id>/delete/", views.delete_task, name="delete"),
    path("clear-completed/", views.clear_completed, name="clear_completed"),
]
