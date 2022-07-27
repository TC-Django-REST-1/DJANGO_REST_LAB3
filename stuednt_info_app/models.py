from django.db import models

# Create your models here.

class Student(models.Model): 

    firstname = models.CharField(max_length=32, null=False)
    lastname = models.CharField(max_length=32, null=False)
    birthdate = models.DateField(null=False)
    GBA = models.FloatField(null=False)