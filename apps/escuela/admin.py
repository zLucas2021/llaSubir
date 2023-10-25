from django.contrib import admin
from .models import Escuela
# Register your models here.
@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    list_display = ['nombre','ubicacion','cant_mesas']
    search_fields = ['nombre',]
