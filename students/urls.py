from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path('create', views.add_Student, name="add_student"),
    path('list', views.list_Student, name="list_student"),
    path('update/<student_id>', views.update_student, name='update_student'),
    path('delete/<student_id>', views.delete_student, name='delete_student'),
]
