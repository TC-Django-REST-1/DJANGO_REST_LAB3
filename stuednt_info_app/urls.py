from django.urls import path
from . import views

app_name = "student_info_app"

urlpatterns = [
  path("add/", views.add_student, name="add student"),
  path("all/", views.all_students, name="all student"),
  path("update/<int:student_id>", views.update_student, name="update student"),
  path("delete/<int:student_id>", views.delete_student, name="delete student"),
]