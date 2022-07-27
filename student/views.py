from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
from .models import Student

@api_view(['POST'])
def add_student(request : Request):
  try:
    fname = request.data["first name"]
    lname = request.data["last name"]
    birth_date = request.data["birth date"]
    gpa = request.data["gpa"]
    new_student = Student(first_name=fname, last_name=lname, birth_date=birth_date, gpa=gpa)
    new_student.save()
    return Response({"msg" : "Student added successfully!"})
  except Exception as e:
    print(e)
    return Response({"msg" : "Process failed!"}, status=400)

@api_view(['GET'])
def list_students(request : Request):
  try:
    students = Student.objects.all()
    return Response({
      "msg" : "A list of all students",
      "students" : [{
        "student id" : student.id,
        "first name" : student.first_name,
        "last name" : student.last_name,
        "birth date" : student.birth_date,
        "gpa" : student.gpa
      } for student in students]
    })
  except Exception as e:
    print(e)
    return Response({"msg" : "Process failed!"}, status=400)

@api_view(['PUT'])
def update_student(request : Request, student_id):
  try:
    fname = request.data["first name"]
    lname = request.data["last name"]
    birth_date = request.data["birth date"]
    gpa = request.data["gpa"]
    student = Student.objects.get(id=student_id)
    student.first_name = fname
    student.last_name = lname
    student.birth_date = birth_date
    student.gpa = gpa
    student.save()
    return Response({"msg" : "Student's information is updated successfully"})
  except Exception as e:
    print(e)
    return Response({"msg" : "Process failed!"}, status=400)

@api_view(['DELETE'])
def delete_student(request : Request, student_id):
  try:
    Student.objects.get(id=student_id).delete()
    return Response({"msg" : "Student is deleted successfully"})
  except Exception as e:
    print(e)
    return Response({"msg" : "Student is not in the database!"})
