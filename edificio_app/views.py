from django.shortcuts import render
from django.http import HttpResponse , JsonResponse


# Create your views here.

def loginView(request):
    return render (request, 'login.html')

def indexView(request):
    return render (request, 'index.html')