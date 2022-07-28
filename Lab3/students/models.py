from django.db import models

# Create your models here.
from pydoc import describe
from pyexpat import model

class Student(models.Model):
    first_name= models.CharField(max_length=512)
    last_name=models.CharField(max_length=512)
    birth_date= models.DateField()
    gpa =models.FloatField()

