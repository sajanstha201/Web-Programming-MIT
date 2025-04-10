from rest_framework import serializers
from .models import *
class workSerializer(serializers.ModelSerializer):
    class Meta:
        model=workModel
        fields='__all__'
        
class liveSerializer(serializers.ModelSerializer):
    class Meta:
        model=livesModel
        fields='__all__'