from rest_framework import routers, serializers, viewsets

#Importancion de modelos
from Categorias.models import CategoriasModel

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasModel
        fields = ('__all__')
        