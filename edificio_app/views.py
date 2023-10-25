from django.shortcuts import render
from django.http import HttpResponse , JsonResponse


# Create your views here.

def loginView(request):
    return render (request, 'login.html')