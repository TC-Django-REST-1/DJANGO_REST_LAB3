from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Student
# Create your views here.


@api_view(['POST'])
def create_student(request: Request):
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    birth_date = request.data['birth_date']
    gpa = request.data['gpa']

    student = Student(first_name=first_name, last_name=last_name,
                      birth_date=birth_date, gpa=gpa)
    student.save()

    response_data = {
        "msg": "student created successfully."
    }

    return Response(response_data)

@api_view(['GET'])
def list_students(request:Request):

    all_students = Student.objects.all()
    list_of_students = [{"firstname":student.firstname,"lastname":student.lastname,"birth_date":student.birth_date,"GPA":student.GPA} 
    for student in all_students]

    response_data = {
        "msg" : "All Students List",
        "Students": list_of_students
    }
    
    
@api_view(['PUT'])
def update_student(request: Request, student_id):

    first_name = request.data['first_name']
    last_name = request.data['last_name']
    birth_date = request.data['birth_date']
    gpa = request.data['gpa']

    student = Student.objects.get(id=student_id)

    student.first_name = first_name
    student.last_name = last_name
    student.birth_date = birth_date
    student.gpa = gpa

    student.save()

    response_data = {
        "msg": f"updated student {student.id}",
    }

    return Response(response_data)

@api_view(['DELETE'])
def delete_student(request: Request, student_id):

    student = Student.objects.get(id=student_id)
    student.delete()

    response_data = {
        "msg": f"deleted student {student_id}",
    }

    return Response(response_data)