from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
@api_view(['POST'])
def create(request : Request):
  try:
    first_name = request.data["first_name"]
    lname = request.data["last_name"]
    birth_date = request.data["birth_date"]
    gpa = request.data["gpa"]

    create_student = Student(first_name=first_name, last_name=lname, birth_date=birth_date, gpa=gpa)
    
    create_student.save()
    
    msg={"msg" : "created Student successfully!"}
    return Response(msg)
  
  except Exception :
    msg={"msg" : "opps! , create was faild"}
    return Response(msg)


@api_view(['GET'])
def list(request : Request):
  try:
    all_students = Student.objects.all()
   
    all_students_list =[{
        "id" : student.id,
        "first_name" : student.first_name,
        "last_name" : student.last_name,
        "birth_date" : student.birth_date,
        "gpa" : student.gpa} 
        for student in all_students]

    msg = {
    "msg" : "list of all students",
    "students" : all_students_list
    }
    
    return Response (msg)
  
  except Exception :
    msg={"msg" : "opps! , retrieve was faild"}
    return Response(msg)

@api_view(['PUT'])
def update(request : Request, student_id):
  try:
    first_name = request.data["first_name"]
    last_name = request.data["last_name"]
    birth_date = request.data["birth_date"]
    gpa = request.data["gpa"]

    student = Student.objects.get(id=student_id)
    student.first_name = first_name
    student.last_name = last_name
    student.birth_date = birth_date
    student.gpa = gpa
    
    student.save()

    msg= {"msg" : "information was updated successfully"}
    
    return Response(msg)

  except Exception :
   
    msg={"msg" : "opps! , update  faild"}
    
    return Response(msg)

@api_view(['DELETE'])
def delete(request : Request, student_id):
  try:
    student=Student.objects.get(id=student_id)
    student.delete()
    msg= {"msg" : "information was updated successfully"}
    return Response(msg)
  
  except Exception : 
    msg={"msg" : "opps! , delet faild"}
    return Response(msg)