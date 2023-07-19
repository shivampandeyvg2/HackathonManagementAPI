from pyexpat import model

from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField

from Hackathon_API.models import Hackathon


class HackathonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'