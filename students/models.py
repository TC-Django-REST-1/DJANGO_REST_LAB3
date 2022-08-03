from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    birth_date = models.DateField()
    GPA = models.FloatField()


    
