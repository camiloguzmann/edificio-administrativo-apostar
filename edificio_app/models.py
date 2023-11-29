from django.db import models
from .choices import options_Equipos
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def _create_user(self,username,email,nombres,password,is_staff,is_superuser,**extra_fields):
        user = self.model(
            username = username,
            email = email,
            nombres = nombres,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self,username,email,nombres,password = None,**extra_fields):
        return self._create_user(username,email,nombres,password,False,False,**extra_fields)
    
    def create_superuser(self,username,email,nombres,password = None,**extra_fields):
        return self._create_user(username,email,nombres,password,True,True,**extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de Usuario',unique=True,max_length=100)
    email = models.EmailField('Correo Electronico',unique=True,max_length=254)
    nombres = models.CharField('Nombres', blank= True , null=True ,max_length=255)
    apellidos = models.CharField('Apellidos', blank= True , null=True ,max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres','apellidos']

    def __str__(self):
        return f'Usuario {self.nombres}.{self.apellidos}'

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