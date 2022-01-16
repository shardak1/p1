from django.db import models

# Create your models here.
class Student(models.Model):
    First_name = models.CharField(max_length=100)
    Middle_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)

