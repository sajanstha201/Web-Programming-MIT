from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework import status
from .serializer import *
def homepage(request):
    print("hello")
    return render(request,"index.html")
def addData(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        # Extract values
        person_name = data.get('person_name')
        companry_name = data.get('companry_name')
        salary = data.get('salary')
        city = data.get('city')
        street = data.get('street')

        # Create workModel first
        work_data = {
            'person_name': person_name,
            'companry_name': companry_name,
            'salary': salary
        }
        work_serializer = workSerializer(data=work_data)

        if work_serializer.is_valid():
            work_instance = work_serializer.save()  # Save and get the instance

            # Now create livesModel using work_instance as ForeignKey
            live_data = {
                'person_name': work_instance.id,  # ForeignKey expects ID or instance
                'city': city,
                'street': street
            }
            live_serializer = liveSerializer(data=live_data)

            if live_serializer.is_valid():
                live_serializer.save()
                return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)
            else:
                print(live_serializer.errors)
                return JsonResponse({'status': 'error', 'details': live_serializer.errors}, status=400)

        else:
            print(work_serializer.errors)
            return JsonResponse({'status': 'error', 'details': work_serializer.errors}, status=400)

    return JsonResponse({'status': 'error'}, status=400)

def getData(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        city = data['city']
        company = data['company']

        # Filter workModel based on related livesModel's city and company's name
        queryset = workModel.objects.filter(
            companry_name=company,
            livesmodel__city=city  # reverse lookup via related_name (default is lowercased model name)
        ).distinct()

        print(queryset)

        serializer = workSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    return JsonResponse({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)

        