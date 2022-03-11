from django.urls import path, re_path
from django.conf.urls import include


#Importacion de vistas
from UsuarioLogin.views import LoginAuth

urlpatterns = [
    re_path(r'^user', LoginAuth.as_view()),
]