from django.urls import path
from . import views

app_name = "studentInfo_app"

urlpatterns = [
    path("create/", views.create_student, name="create_st"),
    path("list/", views.list_students, name="list_st"),
    path("update/<student_id>/", views.update_student, name="update_st"),
    path("delete/<student_id>/", views.delete_student, name="delete_st")
]