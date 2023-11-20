from typing import Any
import cv2,pytesseract , re
import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse , HttpResponseRedirect
from .forms import RegistroVisitanteForm , EmpleadoForm
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from .models import Empleado, Salida , Visitantes
from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.

class indexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='SISTEMA DE SEGURIDAD'
        return context

class CreateVisitanteFormView(TemplateView):
    template_name = 'crearVisitante.html'
    form_class = RegistroVisitanteForm

    def get(self, request, *args, **kwargs):
        visitante_form = self.form_class()
        return render(request, self.template_name, {'form': visitante_form})

    def post(self, request, *args, **kwargs):
        visitante_form = self.form_class(request.POST)

        if visitante_form.is_valid():
            visitante_form.save()
            messages.success(request, 'El visitante se ha registrado exitosamente.')
            # return redirect('salida')
        else:
            messages.error(request, 'Hubo un error al procesar el formulario. Por favor, verifica los datos.')

        return render(request, self.template_name, {'form': visitante_form})

def completarCedula(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula', None)
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
        # extraer la cedula sin puntos
        cedula = ''.join(filter(str.isdigit, cedula))

        response_data = {'cedula': cedula}
        
        return JsonResponse(response_data)

def obtener_datos_visitante(request, cedula):
    # Filtrar visitantes por la identificación proporcionada
    visitantes = Visitantes.objects.filter(identificacion=cedula)

    if visitantes.exists():
        # Tomar el primer visitante del conjunto de resultados
        primer_visitante = visitantes.first()

        # Devolver los datos del primer visitante en formato JSON
        data = {
            'existe': True,
            'nombres': primer_visitante.nombres,
            'apellidos': primer_visitante.apellidos,
            'celular': primer_visitante.celular,
        }
    else:
        # No hay visitantes con la identificación proporcionada
        data = {'existe': False}

    return JsonResponse(data)

class VisitantesSalidaView(ListView):
    model = Visitantes
    template_name = 'salidaVisitantes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'VISITANTES SALIDA'
        return context

    def get_queryset(self):
        # Devuelve solo los visitantes que no tienen una salida registrada
        return Visitantes.objects.exclude(salida__isnull=False)

class SalidaView(ListView):
    template_name = 'salidaVisitantes.html'

    def post(self, request, visitante_id, *args, **kwargs):
        visitante = get_object_or_404(Visitantes, pk=visitante_id)

        # Verificar si ya existe una salida para el visitante
        if not Salida.objects.filter(visitante=visitante).exists():
            # Crear una instancia de Salida
            salida = Salida(visitante=visitante)
            salida.save()

            # Añadir un mensaje de éxito
            messages.success(request, 'Se ha registrado la salida del visitante correctamente.')
        else:
            # Añadir un mensaje de advertencia si ya existe una salida
            messages.warning(request, 'El visitante ya ha registrado su salida previamente.')

        return render(request, self.template_name, {'object_list': self.get_queryset(), 'titulo': 'VISITANTES SALIDA'})

    def get_queryset(self):
        return Visitantes.objects.exclude(salida__isnull=False)

class EmpleadoslistView(ListView):
    model = Empleado
    template_name = 'empleados.html'  
    context_object_name = 'empleados'
    paginate_by = 15

    def get_queryset(self):
        return Empleado.objects.all()
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='EMPLEADOS'
        return context

def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha editado el empleado correctamente.')
            return HttpResponseRedirect(reverse('empleados'))
    else:
        form = EmpleadoForm(instance=empleado)

    return render(request, 'empleados/editarEmpleados.html', {'form': form, 'empleado': empleado})

def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)

    if request.method == 'GET':
        empleado.delete()
        messages.success(request, 'El empleado se eliminó correctamente.')

        # Aquí determinas a dónde redirigir después de la eliminación.
        # Por ejemplo, podrías redirigir a la página principal ('index') o donde desees.
        return HttpResponseRedirect(reverse('empleados'))

    return redirect('empleados')

class CreateEmpleadoFormView(TemplateView):
    template_name = 'empleados/createEmpleados.html'
    form_class = EmpleadoForm

    def get(self, request, *args, **kwargs):
        empleado_form = self.form_class()
        return render(request, self.template_name, {'form': empleado_form})

    def post(self, request, *args, **kwargs):
        empleado_form = self.form_class(request.POST)

        if empleado_form.is_valid():
            empleado_form.save()
            messages.success(request, 'El empleado se ha creado exitosamente.')
            return redirect('index')  # Redirige a la página principal o donde desees después de crear un empleado
        else:
            messages.error(request, 'Hubo un error al procesar el formulario. Por favor, verifica los datos.')

        return render(request, self.template_name, {'form': empleado_form})

class ReportesView(TemplateView):
    template_name = 'reportes.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='REPORTES'
        return context

class UsersView(TemplateView):
    #cuando edite eso cambiar el parametro de TemplateView a ListView
    template_name = 'users.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='LISTA DE USUARIOS'
        return context

class EmpleadosCreateView(TemplateView):
    template_name = 'empleados/createEmpleados.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='CREAR EMPLEADOS'
        return context
    
class EmpleadosEditView(TemplateView):
    template_name = 'empleados/editarEmpleados.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='EDITAR EMPLEADOS'
        return context
    
class UsersCreateView(TemplateView):
    template_name = 'users/createUsers.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='CREAR USUARIOS'
        return context