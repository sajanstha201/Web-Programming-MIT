import json
from django.shortcuts import render
from django.http import JsonResponse

def homePage(request):
    return render(request, "index.html")
def displayPage(request):
    return render(request,"display.html")