from django.urls import path, re_path
from django.conf.urls import include
from IndicadoresDinero.views import IndicadoresView, IndicadoresViewDetail

#Importacion de vistas

urlpatterns = [
    re_path(r'^dinero/(?P<pk>\d+)$', IndicadoresViewDetail.as_view()),
    re_path(r'^dinero', IndicadoresView.as_view()),
]