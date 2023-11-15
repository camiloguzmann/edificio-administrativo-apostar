"""
URL configuration for edificio_administrativo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from edificio_app import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # path('', RedirectView.as_view(url='login/', permanent=False), name='login'),
    path('admin/', admin.site.urls),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('', login_required(views.indexView), name='index'),
    path('visitantes/create/', login_required(views.createFormView), name='create'),
    path('visitantes/salida/', login_required(views.visitantesView), name='visitantes'),
    path('visitantes/empleados/', login_required(views.empleadosView), name='empleados'),
    path('visitantes/reportes/', login_required(views.reportesView), name='reportes'),
    path('visitantes/users/', login_required(views.usersView), name='users'),
    path('empleados/create/', login_required(views.empleadosCreateView), name='crearEmpleados'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cedula/',views.completarCedula)

]
