from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('add/', views.add_book, name='add'),
    path('', views.list_books, name='list_books'),
    path('update/<id>/', views.update_book, name='update_book'),
    path('delete/<id>/', views.delete_book, name='delete_book'),
]
