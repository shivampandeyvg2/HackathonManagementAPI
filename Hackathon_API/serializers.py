from pyexpat import model

from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField
from rest_framework_simplejwt.tokens import RefreshToken

from Hackathon_API.models import Hackathon


class HackathonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'


class CustomTokenObtainPairSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @classmethod
    def get_token(cls, user):
        refresh = RefreshToken.for_user(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return data
