from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Students

# Create your views here.
@api_view(["POST"])
def add_student(request : Request):

    fname = request.data['fname']
    lname = request.data['lname']
    bdate = request.data['bdate']
    gpa = request.data['gpa']

    students = Students(first_name=fname, last_name=lname, birth_date=bdate, GPA=gpa)
    students.save()

    res_data = {

        "msg" : "student added successfully!"
    }
        
    
    return Response(res_data)


@api_view(["GET"])
def list_students(request : Request):

    all_students = Students.objects.all()

    list_all = [{"id": student.id, "full name" : student.first_name + " " + student.last_name , "Birth_date" : student.birth_date, "GPA" : student.GPA }
     for student in all_students]  # This step to convert model data to json data and get it at rest_api

    res_data = {
        'msg' : 'list all students',
        'students' : list_all
    }

    return Response(res_data)


@api_view(["PUT"])
def update_student(request : Request, student_id):

    
    # store json data in request.data

    fname = request.data['fname']
    lname = request.data['lname']
    bdate = request.data['bdate']
    gpa = request.data['gpa']

    # get id of student who will change her info

    student = Students.objects.get(id=student_id)

    # here to assign json data updated to data model of student
    student.first_name = fname
    student.last_name = lname
    student.birth_date = bdate
    student.GPA = gpa

    # save changes
    student.save()

    res_data = {
        'msg' : f'student with id ({student_id}) updated successfully!'
    }

    return Response(res_data)


@api_view(["DELETE"])
def delete_student(request : Request, student_id):

    # get student with id to delete it
    student = Students.objects.get(id=student_id)
    
    
    # get info of student will be delete it
    student_deleted = {'id': student.id, 'name': student.first_name + ' ' + student.last_name, 'birthDate' : student.birth_date} 

    # then delete this student
    student.delete()

    res_data = {
        'msg' : 'student with id ({student_id}) deleted successfully!',
        'student deleted' : student_deleted
    }

    return Response(res_data)
