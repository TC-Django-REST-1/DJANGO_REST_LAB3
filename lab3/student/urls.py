from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('list/', views.list, name="list"),
    path('update/<student_id>/', views.update, name="update"),
    path('delete/<student_id>/', views.delete, name="delete"),
]