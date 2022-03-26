from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class IndicadoresModel(models.Model):
    tipo = models.CharField(max_length = 50, null = False, default="")
    razon_social = models.CharField(max_length = 50, null = False)
    mes = models.CharField(max_length=50, null=False, default="")
    semana1 = models.DecimalField(max_digits=18 ,decimal_places=2 ,null = True, default=0 ,validators=[MinValueValidator(0.01)])
    semana2 = models.DecimalField(max_digits=18 ,decimal_places=2 ,null = True, default=0 ,validators=[MinValueValidator(0.01)])
    semana3 = models.DecimalField(max_digits=18 ,decimal_places=2 ,null = True, default=0 ,validators=[MinValueValidator(0.01)])
    semana4 = models.DecimalField(max_digits=18 ,decimal_places=2 ,null = True, default=0 ,validators=[MinValueValidator(0.01)])
    semana5 = models.DecimalField(max_digits=18 ,decimal_places=2 ,null = True, default=0 ,validators=[MinValueValidator(0.01)])
