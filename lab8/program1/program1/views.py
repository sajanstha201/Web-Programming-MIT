from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from .serializers import DIRserializer
from .models import DIR
import json
def homepage(request):
    return render(request,"index.html")
def getData(request):
    if request.method =='GET':
        data=DIR.objects.all()
        serializer=DIRserializer(data,many=True)
        return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
def handleURL(request):
    if request.method =='POST':
        data=json.loads(request.body)
        obj=DIR.objects.get(pk=data['id'])
        obj.num_visited=obj.num_visited+1
        obj.save()
        serializer=DIRserializer(obj)
    return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
def handleLike(request):
    if request.method =='POST':
        data=json.loads(request.body)
        obj=DIR.objects.get(pk=data['id'])
        print(obj.num_like)
        obj.num_like=obj.num_like+1
        print(obj)
        obj.save()
        serializer=DIRserializer(obj)
    return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)