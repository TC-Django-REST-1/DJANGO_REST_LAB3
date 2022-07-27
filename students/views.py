from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Students
from django.core import serializers


@api_view(['POST'])
def add_Student(request: Request):
    fName = request.data['first_name']
    lName = request.data['last_name']
    birth_Date = request.data['birth_date']
    GPA = request.data['GPA']

    new_student = Students(first_name=fName, last_name=lName,
                           birth_date=birth_Date, GPA=GPA)
    new_student.save()

    return Response({
        "msg": "Created student Successfully"
    })


@api_view(["GET"])
def list_Student(request: Request):
    all_Student = Students.objects.all()

    return Response({
        "msg": "This is a list of All Students",
        "student": all_Student.values()
    })


@api_view(['PUT'])
def update_student(request: Request, student_id):

    fName = request.data['first_name']
    lName = request.data['last_name']
    birth_Date = request.data['birth_date']
    GPA = request.data['GPA']

    student = Students.objects.get(id=student_id)

    student.first_name = fName
    student.last_name = lName
    student.birth_date = birth_Date
    student.GPA = GPA

    student.save()

    return Response({"msg": f"the student of the {student_id=} is updated !"})


@api_view(["DELETE"])
def delete_student(request: Request, student_id):
    try:
        student = Students.objects.get(id=student_id)
        temp =student
        student.delete()
    except Exception as e:
        return Response({"msg": "The student is not Found!"})

    return Response({"msg": f"delete the following student {temp.first_name}"})
