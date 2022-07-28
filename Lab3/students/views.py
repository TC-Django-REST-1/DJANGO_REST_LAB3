from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Student
from hashlib import new


# Create your views here.

@api_view(['POST'])
def create_student(request : Request):
    try:
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        birth_date = request.data['birth_date']
        gpa = request.data['gpa']

        new_stundet = Student(first_name=first_name, last_name=last_name, birth_date=birth_date, gpa=gpa)
        new_stundet.save()

        res_data = {
            "msg":f"Student: {new_stundet.first_name} {new_stundet.last_name} has been added"
        }
    except:
        res_data = {
            "msg":"Fail to add student, please pass correct request body."
        }

    return Response(res_data)

@api_view(['GET'])
def list_student(request : Request):
    all_student=Student.objects.all()
    all_student=[{
            "first_name":student.first_name,
            "last_name":student.last_name,
            "birth_date":student.birth_date,
            "gpa":student.gpa } for student in all_student
        ]
    res_data={
        "msg":"A list of All Students ",
        "List" : all_student
        
    }
    return Response(res_data)


@api_view(['PUT'])
def update_student(request : Request ,stu_id ):
    try:
        Stu = Student.objects.get(id=stu_id)
    except:
        res_data = {
            "msg":"Fail to found student! "
        }
        return Response(res_data)
    Stu.first_name = request.data['first_name']
    Stu.last_name = request.data['last_name']
    Stu.birth_date = request.data['birth_date']
    Stu.gpa = request.data['gpa']
    Stu.save()

    res_data = {
            "msg":"Updated ! "
        }
    return Response(res_data)
    

@api_view(['DELETE'])

def delete_student(request : Request, stu_id ):

    try:
        student = Student.objects.get(id=stu_id)
        student.delete()
    except Exception as e:
        return Response({"msg" : "The student is not Found!"})

    return Response({"msg" : f"delete the following student {student.first_name}"}) 


