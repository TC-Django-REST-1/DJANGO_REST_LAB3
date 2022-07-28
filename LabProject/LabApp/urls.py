from django.urls import path
from . import views

app_name = "LabApp"

urlpatterns = {
    path("add_student/", views.add_student),
    path("list_student/", views.list_student),
    path("update_info/", views.update_info),
    path("del_student/", views.del_student)
}