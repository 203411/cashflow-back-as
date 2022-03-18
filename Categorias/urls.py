from django.urls import path, re_path
from django.conf.urls import include
from Categorias.views import CategoriasView,CategoriasViewDetail,CategoriaEntrada,CategoriaGasto, CategoriaCosto

#Importacion de vistas

urlpatterns = [
    re_path(r'^options/(?P<pk>\d+)$', CategoriasViewDetail.as_view()),
    re_path(r'^options', CategoriasView.as_view()),
    re_path(r'^entrada', CategoriaEntrada.as_view()),
    re_path(r'^gasto', CategoriaGasto.as_view()),
    re_path(r'^costo', CategoriaCosto.as_view()),
]