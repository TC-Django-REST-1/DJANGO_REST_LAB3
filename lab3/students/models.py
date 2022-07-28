from django.db import models

# Create your models here.
class student(models.Model):
    fname = models.CharField(max_length=512)
    lname = models.CharField(max_length=512)
    dob = models.DateField()
    gpa = models.FloatField()