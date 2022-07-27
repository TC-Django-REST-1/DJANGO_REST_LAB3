from django.urls import  path
from .views import Students, Student

urlpatterns = [
    path("students/", Students.as_view(), name="students"),
    path("students/<int:pk>/", Student.as_view(), name="student"),
    
]
