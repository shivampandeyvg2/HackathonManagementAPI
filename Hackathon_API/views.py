from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Hackathon, HackathonRegistrationsModel
from .serializers import HackathonDataSerializer, HackathonRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsHackathonCreator


class hackathon_details(APIView):
    permission_classes = [IsAuthenticated]
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

        serializer = HackathonDataSerializer(existingHackathonDetails, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username or password can not be empty'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        data = {
            'user_id': user.id,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(data, status=status.HTTP_200_OK)


class register(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        usertype = request.data.get('usertype')
        if not username or not password or not email:
            return Response({'error': 'Missing username or password or email'}, status=status.HTTP_400_BAD_REQUEST)
        groups = []
        if usertype == 'creator':
            groups.append('hackathon_masters')
        if usertype == 'participant':
            groups.append('hackathon_participants')
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            for group_name in groups:
                group, created = Group.objects.get_or_create(name=group_name)
                user.groups.add(group)
            if usertype == 'admin':
                user.is_superuser = True
                user.is_staff = True
                user.save()
            refresh = RefreshToken.for_user(user)
            data = {
                'user_id': user.id,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class hackathonRegistration(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        existing_data = HackathonRegistrationsModel.objects.filter(hackathon_id=request.data.get('hackathon_id') , registered_usr_id= request.data.get('registered_usr_id') )
        if existing_data.exists():
            return Response({"message": "you are already registered to hackathon"}, status=status.HTTP_208_ALREADY_REPORTED)
        serializer = HackathonRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "you are successfully registered to hackathon"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self , request , pk):
        all_registeredhackathons = HackathonRegistrationsModel.objects.filter(registered_usr_id=pk).all()
        all_registeredhackathon_json=HackathonRegistrationSerializer(all_registeredhackathons , many=True)
        return Response(all_registeredhackathon_json.data, status=status.HTTP_200_OK)

    def delete(self , request , user_id , hackathon_id):
        existing_hackathon = HackathonRegistrationsModel.objects.filter(registered_usr_id=user_id , hackathon_id=hackathon_id)
        if existing_hackathon.exists():
           existing_hackathon.delete()
           return Response({"message": "You are successfully unregistered from the given hackathon0"} , status=status.HTTP_200_OK)
        else :
            return Response({"error": "you are not registered for indicated hackathon"}, status=status.HTTP_404_NOT_FOUND)

