from django.urls import path, re_path
from django.conf.urls import include

#Importacion de vistas
from UsuarioRegistro.views import RegisterAPI

urlpatterns = [
    re_path(r'^new/$', RegisterAPI.as_view()),
]