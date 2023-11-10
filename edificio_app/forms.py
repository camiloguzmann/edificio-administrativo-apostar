from django import forms
from .models import Area, Empleado

class RegistroVisitante(forms.Form):
    cedula = forms.CharField(label='Cédula', max_length=12, help_text='Ingrese el número de cédula sin guiones ni puntos', required=True)
    nombre = forms.CharField(label='Nombres', max_length=100, error_messages={
        'required': 'El campo de nombres es obligatorio.',
        'max_length': 'El nombre no puede tener más de 100 caracteres.',
    })
    apellido = forms.CharField(label='Apellidos', max_length=100, required=True)
    celular = forms.IntegerField(label='Celular', help_text='Ingrese el número de celular sin espacios ni guiones', required=True)
    empresa = forms.CharField(label='Empresa', max_length=100, required=True)
    articulo_id = forms.ChoiceField(label='Tipo de Equipo *', choices=[], required=False)
    marca = forms.CharField(label='Marca *', max_length=100)

    area_id = forms.ModelChoiceField(
            queryset=Area.objects.all(),
            label='Área de Visita',
            required=True
        )

    empleado_id = forms.ModelChoiceField(
        queryset=Empleado.objects.all(), 
        label='Empleado',
        required=True
    )
