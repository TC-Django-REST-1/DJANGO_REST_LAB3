from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Student
import json

@api_view(['POST'])
def add_student(request: Request):
    new_student = Student(first_name = request.data["first_name"], last_name = request.data["last_name"], birth_date = request.data["birth_date"], GPA = request.data["GPA"])
    new_student.save()
    response_date = {
        "msg": "A new record has been created"
    }
    return Response(response_date)


@api_view(['GET'])
def list_students(request: Request):
    students = Student.objects.all()
    student_list = [{"id": student.id, "first_name": student.first_name, "last_name": student.last_name,
                     "birth_date": student.birth_date, "GPA": student.GPA} for student in students]

    response_data = {
        "students": student_list
    }
    return Response(response_data)

@api_view(['PUT'])
def update_info(request : Request):
    student = Student.objects.get(id=request.data["student_id"])

    student.first_name = request.data["first_name"]
    student.last_name = request.data["last_name"]
    student.birth_date = request.data["birth_date"]
    student.GPA = request.data["GPA"]
    student.save()

    return Response({"msg" : "Your student information is updated!"})

@api_view(["DELETE"])
def delete_student(request : Request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        student.delete()
    except Exception as e:
        return Response({"msg" : "The student is not Found!"})
    return Response({"msg" : f"delete the following student {student.first_name}"})