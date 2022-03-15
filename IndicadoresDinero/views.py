from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from IndicadoresDinero.models import IndicadoresModel
from IndicadoresDinero.serializers import IndicadoresSerializer

# Create your views here.
class IndicadoresView(APIView):
    def get(self, request, format = None):
        queryset = IndicadoresModel.objects.all()
        serializer = IndicadoresSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, format = None):
        serializer = IndicadoresSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
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
    
    def put(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        serializer = IndicadoresSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format = None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse.delete()
            return Response("Indicador eliminado", status = status.HTTP_202_ACCEPTED)
        return Response("Indicador no encontrado", status = status.HTTP_400_BAD_REQUEST)
    