from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class IndicadoresModel(models.Model):
    tipo = models.CharField(max_length = 50, null = False, default="")
    num_semana = models.IntegerField(null = False, validators=[MinValueValidator(1), MaxValueValidator(4)])
    razon_social = models.CharField(max_length = 50, null = False)
    monto = models.IntegerField(null = False)
    fecha = models.CharField(max_length=50, null=False, default="")
