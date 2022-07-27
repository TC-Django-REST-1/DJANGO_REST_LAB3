from django.urls import path
from . import views

app_name="student"

urlpatterns=[
    path('create/', views.create, name="create"),
    path('list/', views.list, name="list"),
    path('update/<std_id>/', views.update, name="update"),
    path('delete/<std_id>/', views.delete, name="delete")
]