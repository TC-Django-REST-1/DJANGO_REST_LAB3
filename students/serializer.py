from rest_framework.serializers import ModelSerializer
from rest_framework.fields import DateTimeField
from .models import Students

class StudentsSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"