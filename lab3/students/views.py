from pydoc import apropos
import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import student

# Create your views here.

@api_view(["POST"])
def add_stu(request : Request):
    fname = request.data["fname"]
    lname = request.data["lname"]
    dob = request.data["dob"]
    gpa = request.data["gpa"]
    
    new_stu = student(fname=fname,lname=lname,dob=dob,gpa=gpa)
    new_stu.save()
    
    res_data = {
        "msg" : "New Student added"
    }

    return Response(res_data)


@api_view(["GET"])
def list_stu(request : Request):

    all_stu= student.objects.all()

    all_stu_list = [{"fname" : all_stu.fname,"lname" : all_stu.lname,"dob" : all_stu.dob, "gpa" : all_stu.gpa} for student_info in all_stu]
    
    res_data ={
        "msg": "A list of All Students",
        "Students" : all_stu_list
    }

    return Response(res_data)


@api_view(["PUT"])
def update_stu(request : Request, stu_id):
    fname = request.data["fname"]
    lname = request.data["lname"]
    dob = request.data["dob"]
    gpa = request.data["gpa"]

    stu = student.objects.get(id=stu_id)

    stu.fname = fname
    stu.lname = lname
    stu.dob = dob
    stu.gpa = gpa

    stu.save()

    return Response({"msg":"Student is updated"})

@api_view(["DELETE"])
def delete_stu (request : Request, stu_id):

    try:
        stu = student.objects.get(id=stu_id)
        msg = f"delete the following student {stu.fname}"
        stu.delete()
    except Exception as e:
        return Response({"msg" : "The student is not found "})
    return Response({"msg":msg})
    