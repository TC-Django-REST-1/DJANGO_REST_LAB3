# from django.shortcuts import render
from ast import Return
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.

@api_view(["POST"])
def add_student(request: Request) -> Response:

    fname = request.data["firstname"]
    lname = request.data["lastname"]
    dob = request.data["dob"]
    gba = request.data["GBA"]

    student = Student(firstname=fname, lastname=lname, birthdate=dob, GBA=gba)

    student.save()

    return Response({"msg":"Student added succefully"})


@api_view(['GET'])
def all_students(request: Request) -> Response:

    students = Student.objects.all();
    studentsList = [{item.firstname, item.lastname, item.birthdate, item.GBA} for item in students]
    resposne_data = {"students": studentsList}
    return Response(resposne_data)

@api_view(["PUT"])
def update_student(request: Request, student_id) -> Response:

    student = Student.objects.get(id=student_id)

    student.firstname = request.data["firstname"]
    student.lastname = request.data["lastname"]
    student.birthdate = request.data["dob"]
    student.GBA = request.data["GBA"]

    student.save()

    resposne_data = {"msg": f"info has been updated"}

    return Response(resposne_data)

@api_view(["DELETE"])
def delete_student(request : Request, student_id) -> Response:

    student = Student.objects.get(id=student_id)

    student.delete()


    return Response({"msg" :"student has been removed"})