from typing import Any
import cv2,pytesseract , re
import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import RegistroVisitanteForm
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from .models import Empleado, Area , Visitantes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class loginView(ListView):
    template_name = ('login.html')

@login_required
def indexView(request):
    data = {
        'titulo': 'SISTEMA DE SEGURIDAD'
    }
    return render(request, 'index.html', data)

@login_required
def createFormView(request):
    visitante_form = RegistroVisitanteForm()

    if request.method == 'POST':
        visitante_form = RegistroVisitanteForm(request.POST)

        if visitante_form.is_valid():
            visitante_form.save()
            messages.success(request, 'El visitante se ha registrado exitosamente.')
            return redirect('salida')
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


class visitantesSalidaView(ListView):
    model = Visitantes
    template_name = 'visitantes.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='VISITANTES SALIDA'
        return context


# class EmpleadosView(ListView):
#     model = Empleado
#     template_name = 'empleados.html'  
#     context_object_name = 'empleados'
#     paginate_by = 15

#     def get_queryset(self):
#         return Empleado.objects.all()
    
    
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['titulo']='LISTA DE EMPLEADOS'
#         return context

class EmpleadosView(ListView):
    model = Empleado
    template_name = 'empleados.html'
    context_object_name = 'empleados'
    paginate_by = 15

    def get_queryset(self):
        return Empleado.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Crear un objeto Paginator basado en la lista completa de empleados
        empleados_por_pagina = self.paginate_by
        paginator = Paginator(Empleado.objects.all(), empleados_por_pagina)

        # Obtener el número de página desde la solicitud
        page = self.request.GET.get('page', 1)

        try:
            # Obtener la página actual
            empleados = paginator.page(page)
        except PageNotAnInteger:
            # Si la página no es un número, mostrar la primera página
            empleados = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, mostrar la última página
            empleados = paginator.page(paginator.num_pages)

        # Pasa el objeto Paginator a la plantilla
        context['paginator'] = paginator

        # Pasa la lista paginada de empleados al contexto
        context[self.context_object_name] = empleados

        # Otros datos de contexto
        context['titulo'] = 'LISTA DE EMPLEADOS'

        return context



class ReportesView(TemplateView):
    template_name = 'reportes.html'

class UsersView(TemplateView):
    #cuando edite eso cambiar el parametro de TemplateView a ListView
    template_name = 'users.html'

class EmpleadosCreateView(TemplateView):
    template_name = 'empleados/createEmpleados.html'

class EmpleadosEditView(TemplateView):
    template_name = 'empleados/editarEmpleados.html'

class UsersCreateView(TemplateView):
    template_name = 'users/createUsers.html'
