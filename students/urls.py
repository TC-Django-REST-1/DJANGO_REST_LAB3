from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_new_stu, name='add_new_stu'),
    path('display', views.display_students, name='display_students'),
    path('update/<int:stu_id>', views.upadate_info_student, name='upadate_info_student'),
    path('delete/<int:stu_id>', views.delete_student, name='delete_student')
]
