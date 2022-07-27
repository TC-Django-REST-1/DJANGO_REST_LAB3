from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
@api_view(["POST"])
def add_student(request : Request):
    f_name = request.data["first_name"]
    l_name = request.data["last_name"]
    birth_data = request.data["birth_date"]
    gpa = request.data["GPA"]
     
    new_student = Student(first_name = f_name, last_name = l_name, birth_date = birth_data, GPA = gpa)
    new_student.save()

    res_data = {
        "msg": "created a new student"
    }
    return Response(res_data)


@api_view(["GET"])
def list_students(request : Request):
    all_studens = Student.objects.all()
    all_studens_list = [{"id": student.id, "first_name": student.first_name, "last_name": student.last_name,"birth_date": student.birth_date, "GPA": student.GPA} for student in all_studens]
    res_data = {
        "msg": "A list of All students",
        "Students": all_studens_list
    }
    return Response(res_data)

@api_view(["PUT"])
def update_student(request : Request, student_id):
    f_name = request.data["first_name"]
    l_name = request.data["last_name"]
    birth = request.data["birth_date"]
    gpa = request.data["GPA"]

    student = Student.objects.get(id = student_id)

    student.first_name = f_name
    student.last_name = l_name
    student.birth_date = birth
    student.GPA = gpa
    student.save()

    return Response("Student information has been updated!")

@api_view(["DELETE"])
def delete_student(request : Request, student_id):
    try:
        student = Student.objects.get(id = student_id)
        student.delete()
        msg = f"student {student.first_name} {student.last_name} is deleted! "
    except Exception as e:
        return Response({"msg": "This student is not Found!"})
    
    return Response({"msg": msg})





