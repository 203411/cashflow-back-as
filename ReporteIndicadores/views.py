from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from IndicadoresDinero.models import IndicadoresModel
from IndicadoresDinero.serializers import IndicadoresSerializer

# Create your views here.
class PagarView(APIView):
    def get(self, request, format = None):
        queryset = IndicadoresModel.objects.filter(tipo="Cuentas por pagar")
        serializer = IndicadoresSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class CobrarView(APIView):
    def get(self, request, format = None):
        queryset = IndicadoresModel.objects.filter(tipo="Cuentas por cobrar")
        serializer = IndicadoresSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class BancosView(APIView):
    def get(self, request, format = None):
        queryset = IndicadoresModel.objects.filter(tipo="Banco")
        serializer = IndicadoresSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)