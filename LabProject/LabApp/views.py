from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Student

# Create your views here.

@api_view(["POST"])
def add_student(request : Request):
    f_name = request.data["firstName"]
    l_name = request.data["lastName"]
    bdate = request.data["birthDate"]
    gpa = request.data["GPA"]

    new_student = Student(firstName=f_name, lastName=l_name, birthDate=bdate, GPA=gpa)
    new_student.save()

    response_data = {
        "msg": "Added student successfully"
    }
    return Response(response_data)


@api_view(["GET"])
def list_student(request : Request):
    all_students = Student.objects.all()
    
    all_students_list = [{"id": Student.id, "firstName": Student.firstName, "lastName": Student.lastName, "birthDate": Student.birthDate, "GPA": Student.GPA} for Student in all_students]

    response_data ={
        "msg": "A list of all Students",
        "students": all_students_list
    }

    return Response(response_data)

@api_view(["PUT"])
def update_info(request : Request, student_id):

    f_name = request.data["firstName"]
    l_name = request.data["lastName"]
    bdate = request.data["birthDate"]
    gpa = request.data["GPA"]

    student = Student.objects.get(id=student_id)

    Student.firstName = f_name
    Student.lastName = l_name
    Student.birthDate = bdate
    Student.GPA = gpa

    Student.save()

    response_data = { "msg": "student info is updated"}
    return Response(response_data)



@api_view(["DELETE"])
def del_student(request: Request, student_id):
    try:
        Student = Student.objects.get(id=student_id)
        Student.delete()
    except Exception as e:
        return Response({ "msg": "The student is not found!"})
    
    return Response({ "msg": f"delete the student {Student.firstName}"})