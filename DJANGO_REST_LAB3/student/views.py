from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Student

@api_view(['POST'])
def add_std(request):
    fName = request.data["first_name"]
    lName = request.data["last_name"]
    bDate = request.data["birth_date"]
    gpa = request.data["GPA"]
    
    new_student = Student(first_name = fName, last_name = lName, birth_date = bDate, GPA = gpa)
    new_student.save()

    response_data = {"msg" : f"Student {fName} {lName} created successfully!"}
    return Response(response_data)

@api_view(['GET'])
def list_std(request):
    all_std = Student.objects.all()
    
    all_std_list = [{"first_name" : student.first_name, "last_name" : student.last_name, 
    "birth_date" : student.birth_date, "GPA" : student.GPA} for student in all_std]

    response_data = {"msg" : "A list of all students: ",
                     "students" : all_std_list}
    return Response(response_data)

@api_view(['PUT'])
def update_std(request, std_id):

    fName = request.data["first_name"]
    lName = request.data["last_name"]
    bDate = request.data["birth_date"]
    gpa = request.data["GPA"]
    
    student = Student.objects.get(id=std_id)
    student.first_name = fName
    student.last_name = lName
    student.birth_date = bDate
    student.GPA = gpa

    student.save()

    response_data = {"msg" : f"Student {student.first_name} {student.last_name} updated successfully!"}
    return Response(response_data)

@api_view(['DELETE'])
def delete_std(request, std_id):

    student = Student.objects.get(id=std_id)
    student.delete()

    return Response({"msg" : f"Student {student.first_name} {student.last_name} deleted successfully!"})