from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.students_list, name = 'students_list'),
    path('add/', views.create_student, name = 'create_student'),
    path('update/<id>', views.update_student, name = 'update_student'),
    path('delete/<id>', views.delete_student, name = 'delete_student'),

    # path("all/", views.list_books, name="list_books"),
    # path("add/", views.add_book, name="add_book"),
    # path("update/<book_id>/", views.update_book, name="update_book"),
    # path("delete/<book_id>/", views.delete_book, name="delete_book"),
]