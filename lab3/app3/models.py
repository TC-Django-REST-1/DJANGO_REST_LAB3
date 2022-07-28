from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length = 512)
    last_name = models.CharField(max_length = 512)
    birth_date = models.DateField()
    GPA = models.FloatField() 