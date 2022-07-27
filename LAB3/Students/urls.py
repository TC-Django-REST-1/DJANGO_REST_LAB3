from django.urls import path
from . import views

app_name = "Students"


urlpatterns = [
    path("add/", views.add_student, name="student_adding"),
    path("list/", views.list_students, name="student_listing"),
    path("update/<student_id>/", views.update_student, name="student_updating"),
    path("delete/<student_id>/", views.delete_student, name="student_deleting")
]