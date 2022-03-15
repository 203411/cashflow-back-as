from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from FlujoEfectivo.serializers import FlujoSerializer
from FlujoEfectivo.models import FlujoModel
from datetime import datetime

# Create your views here.

class FlujoView(APIView):
    def get(self, request, format = None):
        queryset = FlujoModel.objects.all()
        serializer = FlujoSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, format = None):
        request.data['fecha'] = datetime.now().strftime("%Y/%m/%d")
        serializer = FlujoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class FlujoViewDetail(APIView):
    def get_object(self,pk):
        try:
            return FlujoModel.objects.get(pk=pk)
        except FlujoModel.DoesNotExist:
            return 0
        
    def get(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = FlujoSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("Sin datos", status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        request.data['fecha'] = datetime.now().strftime("%Y/%m/%d")
        serializer = FlujoSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format = None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse.delete()
            return Response("Flujo de efectivo eliminado", status = status.HTTP_202_ACCEPTED)
        return Response("Flujo de efectivo no encontrado", status = status.HTTP_400_BAD_REQUEST)