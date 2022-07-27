from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import StudentInfo
from django.shortcuts import render

# Create your views here.


@api_view(['POST'])
def create_student(request: Request):
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    birth_date = request.data['birth_date']
    gpa = request.data['gpa']

    student = StudentInfo(first_name=first_name, last_name=last_name,
                      birth_date=birth_date, gpa=gpa)
    student.save()

    response_data = {
        "msg": "student created."
    }

    return Response(response_data)


@api_view(['GET'])
def list_students(request: Request):

    students = StudentInfo.objects.all()
    students_arr = [
        {
            "id": s.id,
            "first_name": s.first_name,
            "last_name": s.last_name,
            "birth_date": s.birth_date,
            "gpa": s.gpa
        }
        for s in students]

    response_data = {
        "msg": f"found {len(students)} students.",
        "students": students_arr
    }

    return Response(response_data)


@api_view(['PUT'])
def update_student(request: Request, student_id):

    first_name = request.data['first_name']
    last_name = request.data['last_name']
    birth_date = request.data['birth_date']
    gpa = request.data['gpa']

    student = StudentInfo.objects.get(id=student_id)

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

    student = StudentInfo.objects.get(id=student_id)
    student.delete()

    response_data = {
        "msg": f"deleted student {student_id}",
    }

    return Response(response_data)
