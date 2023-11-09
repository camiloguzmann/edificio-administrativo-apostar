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
    area = forms.ModelChoiceField(queryset=Area.objects.all(), label='Área de Visita')
    empleado = forms.ModelChoiceField(queryset=Empleado.objects.all(), label='Empleado')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Puedes personalizar las opciones para tus campos de ChoiceField aquí
        self.fields['articulo_id'].choices = [
            (1, 'Portatil'), 
            (2, 'Tablet'), 
            (3, 'Disco duro')
        ]

        # Dependiendo de tus modelos y relaciones, puedes ajustar este código
        self.fields['empleado'].queryset = Empleado.objects.all()  # Todas los empleados disponibles inicialmente

    # Puedes agregar funciones adicionales aquí para manejar la lógica de dependencias y empleados
