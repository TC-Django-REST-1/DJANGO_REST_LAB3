from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
path('add/', views.add_student, name='add_students'),
path('displayAll/', views.display_students, name='display_students'),
path('update/', views.update_student, name='update_student'),
path('delete/<student_name>/', views.delete_student, name='delete_student'),
]
