from rest_framework import serializers
from .models import DIR
class DIRserializer(serializers.ModelSerializer):
    class Meta:
        model=DIR
        fields='__all__'