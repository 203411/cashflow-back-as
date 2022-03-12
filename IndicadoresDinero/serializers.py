from rest_framework import routers, serializers, viewsets

from IndicadoresDinero.models import IndicadoresModel

class IndicadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicadoresModel
        fields = ('__all__')