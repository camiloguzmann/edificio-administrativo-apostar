from django.db import models
from .choices import options_Equipos
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos,
        )

        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,email,username,nombres,apellidos,password):
        usuario = self.create_user(
            email,
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            password = password
        )
        usuario.usuario_administracion = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de Usuario',unique=True,max_length=100)
    email = models.EmailField('Correo Electronico',unique=True,max_length=254)
    nombres = models.CharField('Nombres', blank= True , null=True ,max_length=255)
    apellidos = models.CharField('Apellidos', blank= True , null=True ,max_length=255)
    is_active = models.BooleanField(default=True)
    usuario_administracion = models.BooleanField(default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres','apellidos']

    def __str__(self):
        return f'Usuario {self.nombres}.{self.apellidos}'
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administracion
    

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