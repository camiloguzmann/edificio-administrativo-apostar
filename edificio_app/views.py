from django.shortcuts import render
from django.http import HttpResponse , JsonResponse


# Create your views here.

def loginView(request):
    return render (request, 'login.html')

def indexView(request):
    return render (request, 'index.html')

def createView(request):
    return render (request, 'create.html')

def empleadosView(request):
    return render (request, 'empleados.html')

def reportesView(request):
    return render (request, 'reportes.html')

def usersView(request):
    return render (request, 'users.html')

def visitantesView(request):
    return render (request, 'visitantes.html')