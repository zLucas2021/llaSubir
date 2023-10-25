from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from apps.escuela.models import Escuela
# Create your models here.
class Fiscal(models.Model):
    ROLE_CHOISE = (
        ('Fiscal de Mesa','Fiscal de Mesa'),
        ('Fiscal General','Fiscal General'),
    )
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True,validators=[MinValueValidator(1000000, message="El DNI debe tener al menos 7 dígitos"),MaxValueValidator(999999999,'El DNI no puede tener mas de 9 dígitos')])
    rol = models.CharField(choices=ROLE_CHOISE,max_length=14)
    escuela = models.ForeignKey(Escuela,on_delete=models.PROTECT)
    class Meta:
        ordering = ['nombre','dni']
        verbose_name_plural  = 'Fiscales'
    def __str__(self):
        return self.nombre