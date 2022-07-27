from django.db import models

class Student(models.Model):
   #attributes 
   firstname = models.CharField(max_length=512)
   lastname = models.CharField(max_length=512)
   birth_date = models.DateField()
   GPA = models.FloatField()
