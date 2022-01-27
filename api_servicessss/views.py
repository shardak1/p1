from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView

import requests


# Create your views here.

class StudentAPI(APIView):

    def get(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            ser = StudentSerializer(stu)
            return Response(ser.data)

        stu = Student.objects.all()
        ser = StudentSerializer(stu, many=True)
        return Response(ser.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deeted'})


def home(req):
    mtd = req.GET.get("m", "2")

    if mtd == "1":  # http://127.0.0.1:8000/?m=1

        url = 'http://127.0.0.1:8000/studentapi/'
        url1 = f'http://{req.META["HTTP_HOST"]}/studentapi/'
        print(url, "\n", url1)

        res = requests.get(url)
        try:
            res = res.json()
        except:
            res = {}

    else:
        a = APIView().initialize_request(req)
        res = StudentAPI().get(a)
        res = res.data

    return render(req, 'home.html', {'response': res})
