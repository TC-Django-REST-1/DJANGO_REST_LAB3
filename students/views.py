from django.urls import is_valid_path
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Students as StudentsModel
from .serializer import StudentsSerializer

class Students(APIView):
    def get(self, _request: Request) -> Response:
        serilaizer = StudentsSerializer(StudentsModel.objects.all(), many=True)
        return Response({"data": serilaizer.data})
    
    def post(self, request: Request) -> Response:
        serilaizer = StudentsSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        else:
            return Response({"msg":serilaizer.error_messages}, status=400)

        
class Student(APIView):
    def get(self, _request: Request, pk: int) -> Response:
        student = StudentsModel.objects.filter(pk=pk).first()
        if student is not None:
            return Response(StudentsSerializer(student).data)
        else:
            return Response({"msg":f"There is no student with `{pk}` id"})
    
    def put(self, request: Request, pk: int) -> Response:
        student: StudentsModel = StudentsModel.objects.filter(pk=pk).first()
        if student is not None:
            serilaizer = StudentsSerializer(data=request.data)
            if serilaizer.is_valid():
                student.first_name = serilaizer.data["first_name"]
                student.last_name = serilaizer.data["last_name"]
                student.birth_date = serilaizer.data["birth_date"]
                student.GPA = serilaizer.data["GPA"]
                student.save()
                return Response(StudentsSerializer(student).data)
            else:
                return Response({"msg": serilaizer.error_messages})
        else:
            return Response({"msg":f"There is no student with `{pk}` id"})
    
    def delete(self, _request: Request, pk: int) -> Response:
        student = StudentsModel.objects.filter(pk=pk).first()
        if student is not None:
            student.delete()
            return Response({"msg":"Deleted successfully"})
        else:
            return Response({"msg":f"There is no student with `{pk}` id"})