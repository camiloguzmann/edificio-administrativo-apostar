from django.db import models
from .choices import options_Equipos

class Visitantes(models.Model):
    identificacion = models.IntegerField()
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    celular = models.IntegerField()
    empresa = models.CharField(max_length=255)
    area_id = models.ForeignKey('Area', on_delete=models.CASCADE)
    empleado_id = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    tipo_equipo = models.CharField(max_length=25, choices=options_Equipos, blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Ingreso')

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Area(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255, default='')
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
   
class Salida(models.Model):
    visitante = models.OneToOneField('Visitantes', on_delete=models.CASCADE)
    fecha_salida = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Salida')