from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("add", views.add_student, name="add_student"),
    path("list", views.list_students, name="list_student"),
    path("update", views.update_info, name="update_info"),
    path("delete/<student_id>", views.delete_student, name="delete_student")
]