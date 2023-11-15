from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse


import cv2
import pytesseract
import re
from django.http import JsonResponse
from django.shortcuts import render
import numpy as np
from .forms import RegistroVisitanteForm
from .models import Empleado, Area
from django.contrib import messages




from django.contrib import messages

@login_required
def createFormView(request):
    visitante_form = RegistroVisitanteForm()

    if request.method == 'POST':
        visitante_form = RegistroVisitanteForm(request.POST)

        if visitante_form.is_valid():
            visitante_form.save()
            messages.success(request, 'El visitante se ha registrado exitosamente.')
            return redirect('empleados')
        else:
            messages.error(request, 'Hubo un error al procesar el formulario. Por favor, verifica los datos.')

    return render(request, 'create.html', {'form': visitante_form})

def completarCedula(request):
    if request.method == 'POST':
        # Procesar la imagen con OCR
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
        # Normalizar espacios en blanco
        text = ' '.join(text.split())

        # Patrón para buscar número de cédula
        cedula_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\d{8})')
        cedula_match = cedula_pattern.search(text)
        cedula = cedula_match.group(1) if cedula_match else 'Número de cédula no encontrado'

        # Patrón para buscar nombres y apellidos
        nombres_patron = re.search(r'Nom?b?r?e?s?\s*([A-Z]+)', text)
        apellidos_patron = re.search(r'NUIP\s+[0-9.-]+\s+([A-Z ]+)', text)

        # Extraer los nombres y apellidos si se encuentran
        nombres = nombres_patron.group(1) if nombres_patron else ''
        apellidos = apellidos_patron.group(1) if apellidos_patron else ''

        # Después de obtener cédula, procesarla para quitar puntos y caracteres no numéricos
        cedula = ''.join(filter(str.isdigit, cedula))

        # Actualizar el formulario con la información extraída

        visitante_form = RegistroVisitanteForm(initial={'cedula': cedula, 'nombre': nombres, 'apellido': apellidos})

        response_data = {'cedula': cedula, 'nombres': nombres, 'apellidos': apellidos}
        return JsonResponse(response_data)

# Create your views here.
def loginView(request):
    return render(request, 'login.html')

@login_required
def indexView(request):
    return render(request, 'index.html')


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

@login_required
def empleadosCreateView(request):
    return render (request, 'empleados/createEmpleados.html')
