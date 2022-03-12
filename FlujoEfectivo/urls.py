from django.urls import path, re_path
from django.conf.urls import include
from FlujoEfectivo.views import FlujoView

#Importacion de vistas

urlpatterns = [
    re_path(r'^efectivo', FlujoView.as_view()),
    # re_path(r'^modificar/(?P<pk>\d+)$', FlujoView.as_view()),
]