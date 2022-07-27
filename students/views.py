from distutils.command.build_scripts import first_line_re
from turtle import setundobuffer
from .models import Student 
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(["POST"])
def create_student(requset : Request):
    
    try:
        first_name = requset.data['first_name']
        last_name = requset.data['last_name']
        birth_date = requset.data['birth_date']
        gpa = requset.data['gpa']
        
        new_students = Student(first_name=first_name, last_name=last_name, birth_date=birth_date, gpa=gpa)
        new_students.save()

        res_data = {
            "msg":f"Student: {new_students.first_name} {new_students.last_name} has been added"
        }

    except:
        res_data = {
            "msg":"Fail to add student, please pass correct request body."
        }
    
    return Response(res_data)
    

@api_view(["GET"])
def list_students(request : Request):
    all_students = Student.objects.all()
    students_list = [
                {
            "first_name":student.first_name,
            "last_name":student.last_name,
            "birth_date":student.birth_date,
            "gpa":student.gpa } for student in all_students
        ]

    res_data = {
        "mag":"A list of all students",
        "books":students_list
    }

    return Response(res_data)

@api_view(["PUT"])
def update_student(request : Request, student_id):
    
    try:
        student = Student.objects.get(id=student_id)
    except:
        res_data = {
            "msg":"Fail to found student, please check provided id."
        }

        return Response(res_data) 

    student.first_name = request.data['first_name']
    student.last_name = request.data['last_name']
    student.birth_date = request.data['birth_date']
    student.gpa = request.data['gpa']
    student.save()

    res_data = {
            "msg":"Student updated successfully"
        }
    
    return Response(res_data)


@api_view(["DELETE"])
def delete_student(request : Request, student_id):
    
    try:
        student = Student.objects.get(id=student_id)
    except:
        res_data = {
            "msg":"Fail to found student, please check provided id."
        }

        return Response(res_data) 

    student.delete()

    res_data = {
            "msg":f"Student {student.first_name} {student.last_name} deleted successfully"
        }
    
    return Response(res_data)