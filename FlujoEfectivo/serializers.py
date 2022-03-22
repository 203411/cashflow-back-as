from rest_framework import routers, serializers, viewsets

#Importancion de modelos
from FlujoEfectivo.models import FlujoModel

class FlujoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlujoModel
        fields = ('__all__')