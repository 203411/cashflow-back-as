from django.urls import path, re_path
from django.conf.urls import include
from ReporteIndicadores.views import PagarView,CobrarView,BancosView

#Importacion de vistas

urlpatterns = [
    re_path(r'^pagar/(?P<mesUser>\d+)$', PagarView.as_view()),
    re_path(r'^cobrar/(?P<mesUser>\d+)$', CobrarView.as_view()),
    re_path(r'^banco/(?P<mesUser>\d+)$', BancosView.as_view()), 
]