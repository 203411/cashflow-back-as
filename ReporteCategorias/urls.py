from django.urls import path, re_path
from django.conf.urls import include
from ReporteCategorias.views import ReporteCategoriasView

urlpatterns = [
    re_path(r'^(?P<mesUser>\d+)$', ReporteCategoriasView.as_view()),
]