from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("add/", views.add_std, name = "add_std"),
    path("list/", views.list_std, name = "list_std"),
    path("update/<std_id>", views.update_std, name = "update_std"),
    path("delete/<std_id>", views.delete_std, name = "delete_std"),
]