
from rest_framework import serializers

from Hackathon_API.models import Hackathon, HackathonRegistrationsModel


class HackathonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'


class HackathonRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonRegistrationsModel
        fields = '__all__'
