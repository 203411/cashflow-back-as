from django.db import models

# Create your models here.
class CategoriasModel(models.Model):
    clasificacion = models.CharField(max_length = 50, null = False)
    descripcion = models.CharField(max_length = 50, null = False)
    sub_categoria = models.CharField(max_length = 50, null = False)