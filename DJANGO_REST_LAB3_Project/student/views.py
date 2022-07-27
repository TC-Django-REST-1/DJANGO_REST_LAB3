from hashlib import new
from re import S
from turtle import st
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Student

@api_view(['POST'])
def create(request: Request):
    first_name = request.data["first_name"]
    last_name = request.data["last_name"]
    birth_date = request.data["birth_date"]
    gpa = request.data["gpa"]

    new_student = Student(first_name=first_name, last_name=last_name, birth_date=birth_date, gpa=gpa)
    new_student.save()

    res_data = {
        "msg" : "Student Created Successfully!"
    }
    return Response(res_data)


@api_view(['GET'])
def list(request: Request):
    
    std_list = Student.objects.all()

    student_list = [{"id":student.id, "first_name":student.first_name, "last_name":student.last_name, "birth_date": student.birth_date, "gpa":student.gpa} for student in std_list]

    res_data = {
        "msg" : "A list of All Students",
        "students" : student_list
    }

    return Response(res_data)


@api_view(['PUT'])
def update(request : Request, std_id):

    student = Student.objects.get(id=std_id)

    student.first_name = request.data["first_name"]
    student.last_name = request.data["last_name"]
    student.birth_date = request.data["birth_date"]
    student.gpa = request.data["gpa"]

    student.save()

    return Response({"msg" : "Your student is updated !"})


@api_view(["DELETE"])
def delete(request : Request, std_id):

    try:
        student = Student.objects.get(id=std_id)
        student.delete()
    except Exception as e:
        return Response({"msg" : "The student is not Found!"})

    return Response({"msg" : f"delete the following student {student.first_name}"})