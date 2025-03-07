from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from rest_framework import status
from .models import *
from .serializer import *
def mainPage(request):
    return render(request,'index.html')

def addStudent(request):
    if(request.method=='POST'):
        data=json.loads(request.body)
        print(data)
        serializers=StudentDetailSerializer(data=data)
        if not serializers.is_valid():
            print(serializers.errors)
        if(serializers.is_valid()):
            serializers.save()
            return JsonResponse({'status':'sucess'},status=status.HTTP_200_OK)
        return JsonResponse({'status':'not valid data'},status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'status':'not post method'},status=status.HTTP_404_NOT_FOUND)

def getStudent(request):
    if(request.method=='GET'):
        students=StudentDetail.objects.all()
        serializers=StudentDetailSerializer(students,many=True)
        return JsonResponse(serializers.data,safe=False,status=status.HTTP_200_OK)
    return JsonResponse({'status':'not get method'},status=status.HTTP_404_NOT_FOUND)