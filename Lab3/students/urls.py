from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path('add/',views.create_student,name="create_student"),
    path('all/',views.list_student,name="list_student("),
    path("update/<stu_id>/", views.update_student, name="update_student"),
    path("delete/<stu_id>/", views.delete_student, name="delete_student"),

]
