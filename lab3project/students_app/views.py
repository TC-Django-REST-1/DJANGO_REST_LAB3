from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
@api_view(['POST'])
def add_student(request:Request):

    firstname = request.data["firstname"]
    lastname = request.data["lastname"]
    birth_date = request.data["birth_date"]
    GPA = request.data["GPA"]

    new_student = Student(firstname = firstname,lastname = lastname, birth_date = birth_date , GPA = GPA)
    new_student.save()

    response_data = {
        "msg" : "Added a Student Successfully"
    }

    return Response(response_data)

@api_view(['GET'])
def get_students(request:Request):

    all_students = Student.objects.all()
    list_of_students = [{"firstname":student.firstname,"lastname":student.lastname,"birth_date":student.birth_date,"GPA":student.GPA} 
    for student in all_students]

    response_data = {
        "msg" : "All Students List",
        "Students": list_of_students
    }

    return Response(response_data)

@api_view(['PUT'])
def update_student(request:Request, student_id):

    student = Student.objects.get(id=student_id)

    student.firstname = request.data["firstname"]
    student.lastname = request.data["lastname"]
    student.birth_date = request.data["birth_date"]
    student.GPA = request.data["GPA"]

    student.save()

    response_data = {
        "msg" : "Student Information Updated!",
       
    }
    return Response(response_data)
@api_view(['DELETE'])
def delete_student (request:Request, student_id):

    student = Student.objects.get(id=student_id)
    student.delete()
        
    response_data = {
        "msg" : "Student Information Deleted!",
       
    }
    return Response(response_data)