from django.http import JsonResponse
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
        result = []
        totales = [0,0,0,0,0,0]
        queryset = IndicadoresModel.objects.filter(Q(tipo="Cuentas por pagar") & Q(mes=mesUser))
        for q in queryset:
            totales[0] += q.semana1
            totales[1] += q.semana2
            totales[2] += q.semana3
            totales[3] += q.semana4
            totales[4] += q.semana5
            totales[5] += q.semana5
        serializer = IndicadoresSerializer(queryset, many = True, context = {'request':request})
        result.append({"pagar" : serializer.data, "totales" : totales})
        return JsonResponse(result,safe=False)
    
class CobrarView(APIView):
    def get(self, request,mesUser, format = None):
        if(len(mesUser) == 1):
            mesUser = "0"+mesUser
        result = []
        totales = [0,0,0,0,0,0]
        queryset = IndicadoresModel.objects.filter(Q(tipo="Cuentas por cobrar") & Q(mes=mesUser))
        for q in queryset:
            totales[0] += q.semana1
            totales[1] += q.semana2
            totales[2] += q.semana3
            totales[3] += q.semana4
            totales[4] += q.semana5
            totales[5] += q.semana5

        serializer = IndicadoresSerializer(queryset, many = True, context = {'request':request})
        result.append({"cobrar" : serializer.data, "totales" : totales})
        return JsonResponse(result,safe=False)
    
class BancosView(APIView):
    def get(self, request,mesUser, format = None):
        if(len(mesUser) == 1):
            mesUser = "0"+mesUser
        result = []
        totales = [0,0,0,0,0,0]
        queryset = IndicadoresModel.objects.filter(Q(tipo="Banco") & Q(mes=mesUser))
        for q in queryset:
            totales[0] += q.semana1
            totales[1] += q.semana2
            totales[2] += q.semana3
            totales[3] += q.semana4
            totales[4] += q.semana5
            totales[5] += q.semana5
        serializer = IndicadoresSerializer(queryset, many = True, context = {'request':request})
        result.append({"bancos" : serializer.data, "totales" : totales})
        return JsonResponse(result,safe=False)