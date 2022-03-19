from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Categorias.serializers import CategoriasSerializer
from Categorias.models import CategoriasModel

from django.db.models import Q
# Create your views here.

class CategoriasView(APIView):
    def get(self, request, format = None):
        queryset = CategoriasModel.objects.all()
        serializer = CategoriasSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def get_object(self,sub_categoria):
        try:
            return CategoriasModel.objects.get(sub_categoria=sub_categoria)
        except CategoriasModel.DoesNotExist:
            return 0

    def post(self, request, format = None):
        exist = self.get_object(request.data['sub_categoria'])
        if(exist == 0):
            serializer = CategoriasSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Categoria ya registrada", status = status.HTTP_406_NOT_ACCEPTABLE)

class CategoriasViewDetail(APIView):
    def get_object(self,pk):
        try:
            return CategoriasModel.objects.get(pk=pk)
        except CategoriasModel.DoesNotExist:
            return 0
        
    def get(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = CategoriasSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("Sin datos", status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        serializer = CategoriasSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse.delete()
            return Response("Categoria eliminada", status = status.HTTP_202_ACCEPTED)
        return Response("Categoria no encontrada", status = status.HTTP_400_BAD_REQUEST)
    
class CategoriaEntrada(APIView):
    def get(self, request, format = None):
        queryset = CategoriasModel.objects.filter(descripcion = "INGRESO")
        serializer = CategoriasSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)

class CategoriaSalida(APIView):
    def get(self, request, format = None):
        queryset = CategoriasModel.objects.filter(Q(descripcion = "COSTO-VENTA") | Q(descripcion = "GASTO-AOC"))
        serializer = CategoriasSerializer(queryset, many = True, context = {'request':request})
        print(serializer.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
