from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Hackathon
from .serializers import HackathonDataSerializer


class hackathon_details(APIView):
    def post(self, request):
        serializer = HackathonDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        hackathonList = Hackathon.objects.all()
        serializer = HackathonDataSerializer(hackathonList, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            existingHackathonDetails = Hackathon.objects.get(pk=pk)
        except Hackathon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, message="No results found for given Hackathon id ")

        serializer = HackathonDataSerializer(existingHackathonDetails , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
