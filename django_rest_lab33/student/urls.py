from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path('create/', views.create_student, name='create new student'),
    path('list/', views.list_students, name='list all students'),
    path('update/<int:student_id>/', views.update_student, name='update a stundet'),
    path('delete/<int:student_id>/', views.delete_student, name='delete a stundet')
]