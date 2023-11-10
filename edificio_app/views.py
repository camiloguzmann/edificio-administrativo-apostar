from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


import cv2
import pytesseract
import re
from django.http import JsonResponse
from django.shortcuts import render
import numpy as np
from .forms import RegistroVisitante
from .models import Empleado


@login_required
def createFormView(request):
    form = RegistroVisitante()

    if request.method == 'POST':
        form = RegistroVisitante(request.POST)
        if form.is_valid():
            # # Filtrar empleados basados en el área seleccionada
            # area_seleccionada = form.cleaned_data['dependencia_id']
            # empleados_en_area = Empleado.objects.filter(area=area_seleccionada)
            # form.fields['empleado_id'].choices = [(empleado.id, empleado.nombre) for empleado in empleados_en_area]
            # # Restaurar el área seleccionada en el formulario
            # form.fields['dependencia_id'].initial = area_seleccionada
            pass

    return render(request, 'create.html', {'form': form})

def get_empleados(request):
    pass
    # area_id = request.GET.get('area_id')
    # empleados = Empleado.objects.filter(area_id=area_id).values_list('id', 'nombre')
    # empleado_choices = [(id, nombre) for id, nombre in empleados]

    # return JsonResponse({'empleados': empleado_choices})


# Create your views here.
def loginView(request):
    return render(request, 'login.html')

@login_required
def indexView(request):
    return render(request, 'index.html')

def completarCedula(request):
        image = request.FILES['image'].read()
        nparr = np.frombuffer(image, np.uint8)
        imagen = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Convertir a escala de grises
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        # Aplicar filtro de umbral
        umbral = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 55, 25)
        # Configurar OCR
        config = '--psm 1'
        text = pytesseract.image_to_string(umbral, config=config)
        #normalizar espacios en blanco
        text = ' '.join(text.split())
        print(text)

        cedula_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\d{8})')
        cedula_match = cedula_pattern.search(text)
        cedula = cedula_match.group(1) if cedula_match else 'Número de cédula no encontrado'


        # Patrón para buscar nombres y apellidos
        nombres_patron = re.search(r'Nom?b?r?e?s?\s*([A-Z]+)', text)
        apellidos_patron = re.search(r'NUIP\s+[0-9.-]+\s+([A-Z ]+)', text)

        # Extraer los nombres y apellidos si se encuentran
        nombres = nombres_patron.group(1) if nombres_patron else ''
        apellidos = apellidos_patron.group(1) if apellidos_patron else ''

        # Después de obtener cedula, procesarla para quitar puntos y caracteres no numéricos
        cedula = ''.join(filter(str.isdigit, cedula))   

        response_data = {'cedula': cedula, 'nombres': nombres, 'apellidos': apellidos}
        return JsonResponse(response_data)


@login_required
def empleadosView(request):
    return render (request, 'empleados.html')

@login_required
def reportesView(request):
    return render (request, 'reportes.html')

@login_required
def usersView(request):
    return render (request, 'users.html')

@login_required
def visitantesView(request):
    return render (request, 'visitantes.html')

