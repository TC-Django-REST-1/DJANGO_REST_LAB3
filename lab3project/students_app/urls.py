from django.urls import path
from . import views

app_name = "students_app"

urlpatterns = [
    path("add/", views.add_student, name="add_student"),
    path("all/", views.get_students, name="get_students"),
    path("update/<student_id>", views.update_student, name="update_student"),
    path("delete/<student_id>", views.delete_student, name="delete_student"),
]