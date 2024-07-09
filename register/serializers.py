from rest_framework import serializers
from .models import *


class CyberSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CyberSport
        fields = '__all__'

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = '__all__'

class MobilographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobilography
        fields = '__all__'

class RobotixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robotix
        fields = '__all__'

class DroneRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneRace
        fields = '__all__'

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'

class MasterClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterClass
        fields = '__all__'