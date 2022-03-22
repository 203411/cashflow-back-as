from django.urls import path, re_path
from django.conf.urls import include
from ReporteIndicadores.views import PagarView,CobrarView,BancosView

#Importacion de vistas

urlpatterns = [
    re_path(r'^pagar', PagarView.as_view()),
    re_path(r'^cobrar', CobrarView.as_view()),
    re_path(r'^banco', CobrarView.as_view()),
]