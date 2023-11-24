from django.contrib import admin
from .models import Area, Empleado, Visitantes , Salida , Usuario

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('areas',)

    #Esta funcion es para devolver el nombre de un area en mayuscula
    def areas(self, obj):
        return obj.nombre.upper()
    
    areas.admin_order_field = 'nombre'
    
@admin.register(Salida)
class SalidaAdmin(admin.ModelAdmin):
    list_display = ('visitante_nombre', 'visitante_identificacion', 'fecha_salida')

    def visitante_nombre(self, obj):
        return obj.visitante.nombres

    def visitante_identificacion(self, obj):
        return obj.visitante.identificacion

    visitante_nombre.admin_order_field = 'visitante__nombres'
    visitante_identificacion.admin_order_field = 'visitante__identificacion'

@admin.register(Visitantes)
class VisitantesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'identificacion', 'tipo_equipo','created_at')
    list_filter = ('tipo_equipo','created_at')

admin.site.register(Empleado)
admin.site.register(Usuario)