from django.urls import path
from . import views



urlpatterns = [
    path("add/", views.add_student, name="add"),
    path("all/", views.list_students, name="list"),
    path("update/<studnet_id>/", views.update_student, name="update"),
    path("delete/<studnet_id>/", views.delete_student, name="delete"),
]