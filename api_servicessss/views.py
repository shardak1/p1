from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from django.http import HttpResponse
import requests
# Create your views here.

class StudentAPI(APIView):
 def get(self, request, pk=None, format=None):
  id = pk
  if id is not None:
   stu = Student.objects.get(id=id)
   serializer = StudentSerializer(stu)
   return Response(serializer.data)

  stu = Student.objects.all()
  serializer = StudentSerializer(stu, many=True)
  return Response(serializer.data)

def post(self, request, format=None):
 serializer = StudentSerializer(data=request.data)
 if serializer.is_valid():
  serializer.save()
  return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def put(self, request, pk , format=None):
 id = pk
 stu = Student.objects.get(pk=id)
 serializer = StudentSerializer(data=request.data)
 if serializer.is_valid():
  serializer.save()
  return Response({'msg':'Complete Data Updated'})
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def patch(self, request, pk , format=None):
    id = pk
    stu = Student.objects.get(pk=id)
    serializer = StudentSerializer(stu,data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Partial Data Updated'})
    return Response(serializer.errors)

def Delete(self, request, pk , format=None):
    id = pk
    stu = Student.objects.get(pk=id)
    stu.delete()
    return Response({'msg':'Data De;eted'})
def home(request):
    response = requests.get('http://127.0.0.1:8000/studentapi/').json()
    return render(request,'home.html', {'response':response})