from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from IndicadoresDinero.models import IndicadoresModel
from IndicadoresDinero.serializers import IndicadoresSerializer
from django.db.models import Q

# Create your views here.
class PagarView(APIView):
    def get(self, request,mesUser, format = None):
        if(len(mesUser) == 1):
            mesUser = "0"+mesUser
        queryset = IndicadoresModel.objects.filter(Q(tipo="Cuentas por pagar") & Q(fecha__startswith=mesUser))
        serializer = IndicadoresSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class CobrarView(APIView):
    def get(self, request,mesUser, format = None):
        if(len(mesUser) == 1):
            mesUser = "0"+mesUser
        queryset = IndicadoresModel.objects.filter(Q(tipo="Cuentas por cobrar") & Q(fecha__startswith=mesUser))
        serializer = IndicadoresSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class BancosView(APIView):
    def get(self, request,mesUser, format = None):
        if(len(mesUser) == 1):
            mesUser = "0"+mesUser
        queryset = IndicadoresModel.objects.filter(Q(tipo="Banco") & Q(fecha__startswith=mesUser))
        serializer = IndicadoresSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)