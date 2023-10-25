from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


# Create your models here.
class Usuario(AbstractUser):
    """Clase Usuario hereda de AbstractUser para su customizacion"""    
    imagen = models.ImageField(
        null=True, blank=True, upload_to="usuario/", default="../static/usuario/user-default.jpg"
    )
    #rol = models.CharField(max_length=10, choices=ROLE_CHOICES)
    telefono = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0000000000),  # Para evitar valores negativos
            MaxValueValidator(9999999999),  # Máximo de 20 dígitos
            RegexValidator(
                regex=r"^\d{10}$",  # Expresión regular para verificar 10 dígitos exactos
                message="El número de teléfono debe tener exactamente 10 dígitos.",
            ),
        ],
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username
