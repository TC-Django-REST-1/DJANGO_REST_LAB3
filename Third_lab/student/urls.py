from django.urls import path
from . import views
app_name = 'student'

urlpatterns = [
    path('create/', views.create_student, name="create_student"),
    path('list/', views.list_students, name="list_students"),
    path('update/<student_id>/', views.update_student, name="update_student"),
    path('delete/<student_id>/', views.delete_student, name="delete_student"),
]