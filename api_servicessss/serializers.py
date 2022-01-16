from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
 class Meta:
    model = Student
    fields = ['id', 'First_name','Middle_name','Last_name']