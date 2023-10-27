from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginView(request):
    return render(request, 'login.html')

@login_required
def indexView(request):
    return render(request, 'index.html')

@login_required
def createView(request):
    return render (request, 'create.html')

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


