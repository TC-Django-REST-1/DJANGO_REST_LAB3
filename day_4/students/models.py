from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    birth_date = models.DateField()
    GPA = models.FloatField(default=0)
    