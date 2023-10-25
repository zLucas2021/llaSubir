from django.contrib import admin
from .models import Fiscal

@admin.register(Fiscal)
class FiscalAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','dni','rol','escuela']
    list_filter =['escuela',]
    search_fields = ['dni',]
    
