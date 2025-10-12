from django.shortcuts import render
from rest_framework.views import APIView
from .import serializers
class UserRegistrationApiView(APIView):
    serializer_class =serializers.RegistrationSeriarizer
    
