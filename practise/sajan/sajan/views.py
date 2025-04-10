from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .serializer import StudentSerializer
from .models import Student
def home_page(request):
    if(request.method=="POST"):
        data=json.loads(request.body)
        ser=StudentSerializer(data=data)
        if(ser.is_valid()):
            ser.save()
            return HttpResponse(request,'<h1>success</h1>')
        else:
            return JsonResponse({'status':'fail'})
    return render(request,'index.html')
def get_data(request):
    if(request.method=='GET'):
        obj=Student.objects.all()
        ser=StudentSerializer(obj,many=True)
        return JsonResponse(ser.data,safe=False)