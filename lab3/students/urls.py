import imp
from django.urls import URLPattern, path 
from . import views

app_name = "students"

urlpatterns = [
    path("add/", views.add_stu, name="add_stu"),
    path("list/", views.list_stu, name="list_stu"),
   path("update/<stu_id>", views.update_stu, name="update_stu"),
    path("delete/", views.delete_stu, name="delete_stu"),
]

