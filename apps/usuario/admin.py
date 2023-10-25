from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .models import Usuario 

#*Setear los valores para la administracion
admin.site.site_header = 'La Libertad Avanza'
admin.site.site_title = 'Administracion'
admin.site.index_title = 'Bienvenido'
# Register your models here.

@admin.register(Usuario)
class UserAdmin(UserAdmin):
    """
    Clase que registra al modelo Usuario en La administracion
    """
    list_display=('username','telefono')
    fieldsets=(
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'imagen','telefono')}),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ['username',]
    list_filter=[]
    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            # Si es superusuario, puede modificar cualquier perfil de usuario
            return True
        if obj is not None and request.user == obj:
            # El usuario puede modificar su propio perfil
            return True
        if request.user.has_perm('usuario.add_usuario'):
            
            return True
        
        return False
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        # Permitir que el usuario vea pero no modifique la sección de permisos
        if obj is not None and obj == request.user:
            return self.readonly_fields + ('user_permissions', 'is_active', 'is_staff', 'is_superuser','groups','last_login','date_joined')  # Añade 'user_permissions' a los campos de solo lectura
        if request.user.has_perm('usuario.add_usuario') and not request.user.is_superuser:
            return self.readonly_fields + ('email','imagen','telefono','first_name','last_name','user_permissions', 'is_active', 'is_staff', 'is_superuser','groups','last_login','date_joined')
        return self.readonly_fields
    
    get_groups.short_description = 'Grupos'        
