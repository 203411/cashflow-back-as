from django.urls import path, re_path


#Importacion de vistas
from UsuarioRegistro import views

urlpatterns = [
    re_path(r'^lista/',views.user_list), #get y post
     re_path(r'^user/(?P<pk>\d+)$',views.user_detail),#get por user, put,delete
]