from cgitb import reset
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Students


# Create your views here.
@api_view(['POST'])
def add_student(request : Request):
    data = request.data
    student = Students(first_name=data['fName'],last_name=data['lName'],birth_date=data['bDate'],GPA=data['GPA'])
    student.save()

    res = {
        'msg': 'The student add Successfully!'
        }
    return Response(res)

@api_view(['GET'])
def display_students(request : Request):

    students = [{'name':f'{student.first_name} {student.last_name}','Birth Date':student.birth_date,'GPA':student.GPA} for student in Students.objects.all()]

    res = {'msg': 'list of all student',
            'students':students,
          }

    return Response(res)



@api_view(['PUT'])
def update_student(request : Request):
    data = request.data
    student = Students.objects.get(first_name=data['fName'])
    student.first_name = data['fName']
    student.last_name = data['lName']
    student.birth_date = data['BDate']
    student.GPA = data['GPA']

    student.save()

    res = {'msg':'the student info updated Successfully!'}
    return Response(res)



@api_view(['DELETE'])
def delete_student(request : Request, student_name):
    student = Students.objects.get(first_name=student_name)
    
    try:
        student = Students.objects.get(first_name=student_name)
        student.delete()
    except Exception as e:
        return Response({'msg': "The student is not Found!"})
    
    return Response({"msg" : f"The student {student.first_name} {student.last_name} deleted Successfully!"})


