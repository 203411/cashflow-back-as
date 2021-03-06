from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
#from rest_framework import generics
from rest_framework.permissions import AllowAny
#from rest_framework import status
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def user_list(request):
    if request.method == 'GET':
        usuario = User.objects.all()
        serializer = RegisterSerializer(usuario, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        serializer = RegisterSerializer(data=usuario_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def user_detail(request, pk):
    try: 
        usuario = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'No existe el usuario'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        serializer = RegisterSerializer(usuario) 
        return JsonResponse(serializer.data) 

    elif request.method == 'PUT': 
        usuario_data = JSONParser().parse(request) 
        serializer = RegisterSerializer(usuario, data=usuario_data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        usuario.delete() 
        return JsonResponse({'message': 'Usuario a sido eliminado!'}, status=status.HTTP_204_NO_CONTENT)
    
        
