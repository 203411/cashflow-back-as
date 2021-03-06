from django.urls import path, include, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.views.static import serve
from django.conf import settings

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^cash_flow/login/', include('UsuarioLogin.urls')),
    re_path(r'^cash_flow/registro/', include('UsuarioRegistro.urls')),
    re_path(r'^cash_flow/flujo/', include('FlujoEfectivo.urls')),
    re_path(r'^cash_flow/indicadores/', include('IndicadoresDinero.urls')),
    re_path(r'^cash_flow/categorias/', include('Categorias.urls')),
]