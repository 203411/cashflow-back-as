from django.shortcuts import render

# Importaciones
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import generics

# Create your views here.

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
import json 
class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    def get(self, request, format=None):
        queryset=User.objects.all()
        serializer=RegisterSerializer(queryset,many=True, context={'request':request})
        return Response(serializer.data)