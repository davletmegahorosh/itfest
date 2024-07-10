# serializers.py

from rest_framework import serializers
from .models import FoodZone, IT_Expo

class FoodZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodZone
        fields = '__all__'

class ITExpoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_Expo
        fields = '__all__'
