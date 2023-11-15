from django.contrib import admin
from .models import Area, Empleado, Visitantes


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('areas',)

    #Esta funcion es para devolver el nombre de un area en mayuscula
    def areas(self, obj):
        return obj.nombre.upper()
    
    areas.admin_order_field = 'nombre'


admin.site.register(Empleado)
admin.site.register(Visitantes)