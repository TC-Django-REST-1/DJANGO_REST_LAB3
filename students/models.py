from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=30, null=False, help_text="Name of the student")
    last_name = models.CharField(max_length=30, null=False, help_text="Last name of the student")
    birth_date = models.DateField(null=False, help_text="Birth date of the student")
    GPA = models.FloatField(null=False, help_text="GPA of the student")
    