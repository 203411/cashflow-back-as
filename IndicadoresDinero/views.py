from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from IndicadoresDinero.models import IndicadoresModel
from IndicadoresDinero.serializers import IndicadoresSerializer
from datetime import datetime
from django.db.models import Q

# Create your views here.
class IndicadoresView(APIView):
    def get(self, request, format = None):
        queryset = IndicadoresModel.objects.all()
        serializer = IndicadoresSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
class IndicadoresViewDetail(APIView):
    def get_object(self,pk):
        try:
            return IndicadoresModel.objects.get(pk=pk)
        except IndicadoresModel.DoesNotExist:
            return 0
        
    def get(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = IndicadoresSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("Sin datos", status = status.HTTP_400_BAD_REQUEST)
    
    def post(self, request,pk, format = None):
        semana = "semana" + pk
        indicador = IndicadoresModel.objects.filter( Q(razon_social = request.data['razon_social']) & Q(tipo = request.data['tipo']))
        request.data['mes'] = datetime.now().strftime("%m")
        request.data[semana] = request.data['monto']
        if(indicador.exists()):
            if(int(pk) == 1):
                indicador.update(semana1 = request.data['monto'])
            elif(int(pk) == 2):
                indicador.update(semana2 = request.data['monto'])
            elif(int(pk) == 3):
                indicador.update(semana3 = request.data['monto'])
            elif(int(pk) == 4):
                indicador.update(semana4 = request.data['monto'])
            elif(int(pk) == 5):
                indicador.update(semana5 = request.data['monto'])
            print("editar")
            return Response(indicador.values(), status = status.HTTP_201_CREATED)
        else:
            serializer = IndicadoresSerializer(data = request.data)
            print("crear")
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format = None):
        request.data['fecha'] = datetime.now().strftime("%Y/%m/%d")
        idResponse = self.get_object(pk)
        serializer = IndicadoresSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse.delete()
            return Response("Indicador eliminado", status = status.HTTP_202_ACCEPTED)
        return Response("Indicador no encontrado", status = status.HTTP_400_BAD_REQUEST)
    