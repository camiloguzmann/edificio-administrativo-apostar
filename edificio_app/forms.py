from django import forms
from .models import Area, Empleado, Visitantes , Usuario , options_Equipos
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

class RegistroVisitanteForm(forms.ModelForm):
    
    identificacion = forms.IntegerField(label='Cedula',required=True,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca la cedula'}))
    nombres = forms.CharField(label='Nombre', required=True,max_length=25,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Introduzca el nombre'}))
    apellidos = forms.CharField(label='Apellido', required=True,max_length=25,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Introduzca el apellido'}))
    celular = forms.IntegerField(label='Celular',required=True,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca la celular'}))
    empresa = forms.CharField(label='Empresa', required=True,max_length=25,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Introduzca la empresa'}))
    area_id = forms.ModelChoiceField(queryset=Area.objects.all(),label='Área de Visita',required=True,empty_label="Seleccione un área",
    widget=forms.Select(attrs={'class': 'form-control'}))
    empleado_id = forms.ModelChoiceField(queryset=Empleado.objects.all(),label='Empleado',required=True,empty_label="Seleccione un Empleado",
    widget=forms.Select(attrs={'class': 'form-control'}))
    tipo_equipo = forms.ChoiceField(label='Equipo',choices=options_Equipos,required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    marca = forms.CharField(label='Marca',required=False,max_length=10,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca la marca'}))
    serial = forms.CharField(label='serial',required=False,max_length=20,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduzca el serial'}))

    class Meta:
        model = Visitantes
        fields = ['identificacion', 'nombres', 'apellidos', 'celular', 'empresa', 'area_id', 'empleado_id', 'tipo_equipo', 'marca', 'serial']

class EmpleadoForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', required=True,max_length=25,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Introduzca el nombre'}))
    apellido = forms.CharField(label='Apellido', required=True,max_length=25,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Introduzca el apellido'}))
    area = forms.ModelChoiceField(queryset=Area.objects.all(),label='Área de Visita',required=True,empty_label="Seleccione un área",
    widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Empleado
        fields = [ 'nombre', 'apellido', 'area']

class UsuarioForm(forms.ModelForm): 
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese su contraseña...','required':'required'}))
    password2 = forms.CharField(label='Contraseña De Confirmación', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingrese nuevamente su contraseña...','required':'required'}))

    # Campo adicional para elegir el tipo de usuario
    tipo_usuario = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Tipo de Usuario'
    )

    class Meta:
        model = Usuario  
        fields = ['email', 'username', 'nombres', 'apellidos','tipo_usuario']  
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Apellido'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su usuario'}),
        }
