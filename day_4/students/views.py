from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Students

@api_view(['GET'])
def students_list(request: Request):
    all_students = Students.objects.all()
    
    all_students_list = [{ "f_name": all_students.first_name, 'l_name': all_students.last_name, 'birth': all_students.birth_date, 'gpa': all_students.GPA} for student in all_students]

    response_data = {
        'msg': 'Student Information List',
        'student' : all_students_list,
    }

    return Response(response_data)


@api_view(['POST'])
def create_student(request: Request):

    f_name = request.data["first_name"]
    l_name = request.data["last_name"]
    birth = request.data["birth_date"]
    GPA = request.data['GPA']

    new_student = Students(first_name= f_name, last_name= l_name, birth_date= birth, GPA= GPA)
    new_student.save()
    
    response_data = {
        'msg' : 'Student has beed added successfully'
    }

    return Response(response_data)


@api_view(['PUT'])
def update_student(request: Request, id):
    f_name = request.data["first_name"]
    l_name = request.data["last_name"]
    birth = request.data["birth_date"]
    GPA = request.data['GPA']

    student = Students.objects.get(id=id)

    student.first_name = f_name
    student.last_name = l_name
    student.birth_date = birth
    student.GPA = GPA

    student.save()

    return Response({"msg" : "Student has been updated !"})


@api_view(['DELETE'])
def delete_student(request: Request, id):
    try:
        student = Students.objects.get(id=id)
        student.delete()
    except Exception as e:
        return Response({"msg" : "The student is not Found!"})

    return Response({"msg" : f"{student.first_name} {student.last_name} has been deleted"})