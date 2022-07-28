from turtle import st
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Students
from .serializer import StudentSerializer
from django.db.models.functions import Lower


@api_view(['POST'])  # add new student to the databases
def add_Student(request: Request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({
            "msg": "InValid input Successfully"
        })

    return Response({
        "msg": "Created student Successfully"
    })


@api_view(["GET"])
def list_Student(request: Request):
    all_Student = Students.objects.order_by(Lower("first_name"))

    serializer = StudentSerializer(all_Student, many=True)
    return Response({
        "msg": "This is a list of All Students",
        "student": serializer.data
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
        temp = student
        student.delete()
    except Exception as e:
        return Response({"msg": "The student is not Found!"})

    return Response({"msg": f"delete the following student {temp.first_name}"})


@api_view(["patch"])
def patch_student(request: Request, student_id):
    student = Students.objects.get(id=student_id)
    data = request.data
    student.first_name = data.get('first_name', student.first_name)
    student.last_name = data.get('last_name', student.last_name)
    student.birth_date = data.get('birth_date', student.birth_date)
    student.GPA = data.get('GPA', student.GPA)

    student.save()

    serializer = StudentSerializer(student)
    return Response(serializer.data)
