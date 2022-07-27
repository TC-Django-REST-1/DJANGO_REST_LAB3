from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Student


@api_view(["POST"])
def add_student(request : Request):

    first_Name = request.data["firstName"]
    last_Name = request.data["lastName"]
    birth_Date = request.data["birthDate"]
    student_GPA = request.data["GPA"]

    new_student = Student(firstName=first_Name, lastName=last_Name, birthDate=birth_Date, GPA=student_GPA)
    new_student.save()

    res_data = {
        "msg" : "Student Created Successfully"
    }

    return Response(res_data)


@api_view(["GET"])
def list_students(request : Request):

    all_students = Student.objects.all()

    all_Studnets_list = [{"firstName" : student.firstName, "lastName" : student.lastName, "birthDate" : student.birthDate, "GPA": student.GPA} for student in all_students]

    res_data = {
        "msg" : "A list of All Students",
        "studnets" : all_Studnets_list
    }

    return Response(res_data)



@api_view(['PUT'])
def update_student(request : Request, studnet_id):

    first_Name = request.data["firstName"]
    last_Name = request.data["lastName"]
    birth_Date = request.data["birthDate"]
    student_GPA = request.data["GPA"]

    student = Student.objects.get(id=studnet_id)

    student.firstName = first_Name
    student.lastName = last_Name
    student.birthDate = birth_Date
    student.GPA=student_GPA

    student.save()

    return Response({"msg" : "Your Studnet is updated !"})



@api_view(["DELETE"])
def delete_student(request : Request, studnet_id):

    try:
        student = Student.objects.get(id=studnet_id)
        student.delete()
    except Exception as e:
        return Response({"msg" : "The student is not Found!"})

    return Response({"msg" : f"delete the following student {student.firstName}"})