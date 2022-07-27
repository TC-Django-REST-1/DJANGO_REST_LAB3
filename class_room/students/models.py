from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=15,default="")
    last_name = models.CharField(max_length=15,default="")
    birth_date = models.DateField(null=True)
    GPA = models.FloatField(default=5)