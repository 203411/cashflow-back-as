from django.db import models


# Create your models here.
class FlujoModel(models.Model):
    tipo = models.CharField(max_length = 50, null = False)
    id_categoria = models.IntegerField(null = False)
    descripcion = models.CharField(max_length = 50, null = False)
    cantidad = models.IntegerField( null = False)
    fecha = models.CharField(max_length = 50, null = False, default="")