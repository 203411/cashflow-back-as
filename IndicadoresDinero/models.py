from django.db import models

# Create your models here.
class IndicadoresModel(models.Model):
    tipo = models.CharField(max_length = 50, null = False, default="")
    num_semana = models.IntegerField(null = False)
    razon_social = models.CharField(max_length = 50, null = False)
    monto = models.IntegerField(null = False)
    fecha = models.CharField(max_length=50, null=False, default="")
