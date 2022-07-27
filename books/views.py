from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from .models import Books


@api_view(['POST'])
def add_book(request: Request):
    title = request.data['title']
    description = request.data['description']
    rating = request.data['rating']

    book = Books(
        title=title, description=description, rating=rating
        ).save()
    
    return Response({
        "msg": "Book added!"
    })

@api_view(['GET'])
def list_books(request: Request):
    books = {"msg": "there are no books yet!"}
    try:
        books = {
            "books": [
                {"id": book.id, "title": book.title,
                "description": book.description, "rating": book.rating}
                for book in Books.objects.all()
            ]
        }
    except:
        pass

    return Response(books)


@api_view(['PUT'])
def update_book(request: Request, id):
    title = request.data['title']
    description = request.data['description']
    rating = request.data['rating']

    book = Books.objects.get(id=id)

    book.title = title
    book.description = description
    book.rating = rating

    book.save()

    return Response(
        {"msg": "Book updated!"}
    )


@api_view(['DELETE'])
def delete_book(request: Request, id):
    book = get_object_or_404(Books, id=id)
    book.delete()
    return Response(
        {"msg": "Book deleted!"}
    )