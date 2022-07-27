from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Student #استدعاء الكلاس اللي داخل المودل


@api_view(["POST"])
def add_new_stu(request : Request):
    try:
        fname    = request.data["first_name"] 
        lname    = request.data["last_name"]
        birthday = request.data["birthday"]
        GPA      = request.data["GPA"]
    
        new_stu  = Student(first_name = fname,
                           last_name  = lname,
                           birthday   = birthday,
                           GBA        = GPA)
        new_stu.save()

        res_data = {
            "msg" : "Created a new student Successfully"
            }
    except Exception as e:
        res_data = {
            "msg":"Error, please try again!."
        }

        return Response(res_data)
    
    
    
@api_view(['GET'])
def display_students(request : Request):
    
    all_student   = Student.objects.all()
    list_students = [{"id"         : student.id,
                      "first_name" : student.first_name,
                      "last_name"  : student.last_name,
                      "birthday"   : student.birthday,
                      "GPA"        : student.GPA}
                     for student in all_student]
    
    res_data = {
        "msg" : "Display all students",
        "students" : list_students
    }
    return Response(res_data)


@api_view(['PUT'])
def upadate_info_student(request : Request, stu_id):
        fname    = request.data["first_name"] 
        lname    = request.data["last_name"]
        birthday = request.data["birthday"]
        GPA      = request.data["GPA"]
        
        student = Student.objects.get(id = stu_id)
        student.first_name = fname
        student.last_name  = lname
        student.birthday   = birthday
        student.GPA        = GPA
        
        student.save()
        
        res_data = {
        "msg" : "The student you selected is updated",
        }
        return Response(res_data)
   


@api_view(['DELETE'])
def delete_student(request : Request, stu_id):
    try:
        student = Student.objects.get(id = stu_id)
        student.delete()
    except Exception as e:
        return Response({"msg" : "The student is not Found!"})
    return Response({"msg" : f"delete this student {student.first_name}"})
    




