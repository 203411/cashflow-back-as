from django.db import models
<<<<<<< HEAD
=======
from Categorias.models import CategoriasModel
>>>>>>> Develop-Gabriel

# Create your models here.
class FlujoModel(models.Model):
    tipo = models.CharField(max_length = 50, null = False)
<<<<<<< HEAD
    id_categoria = models.IntegerField(null = False)
    descripcion = models.CharField(max_length = 50, null = False)
    cantidad = models.IntegerField( null= False)
=======
    id_categoria = models.ForeignKey(CategoriasModel, on_delete = models.CASCADE, null = False, blank = False)
    descripcion = models.CharField(max_length = 50, null = False)
    cantidad = models.IntegerField( null = False)
    fecha = models.CharField(max_length = 50, null = False, default="")
>>>>>>> Develop-Gabriel
