from django.db import models

# Create your models here.
class Escuela(models.Model):
    nombre = models.CharField(max_length=200,blank=False,null=False)
    ubicacion = models.CharField(max_length=300,null=True,blank=True)
    cant_mesas = models.PositiveIntegerField(null=True,blank=True,default=0)
    def __str__(self):
        return self.nombre
