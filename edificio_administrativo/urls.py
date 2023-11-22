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
from edificio_app.views import *



urlpatterns = [
    # path('', RedirectView.as_view(url='login/', permanent=False), name='login'),
    path('admin/', admin.site.urls),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('', login_required(indexView.as_view()), name='index'),
    path('edificio/visitantes/', login_required(CreateVisitanteFormView.as_view()), name='visitantes'),
    path('edificio/salida/', login_required(VisitantesSalidaView.as_view()), name='salida'),
    path('obtener_datos_visitante/<int:cedula>/', obtener_datos_visitante, name='obtener_datos_visitante'),
    path('salida/<int:visitante_id>/', SalidaView.as_view(), name='salida_visitante'),
    path('edificio/empleados/', login_required(EmpleadoslistView.as_view()), name='empleados'),
    path('edificio/crearEmpleados/', login_required(CreateEmpleadoFormView.as_view()), name='Crearempleados'),
    path('editar_empleado/<int:empleado_id>/', editar_empleado, name='editarEmpleados'),
    path('eliminar_empleado/<int:empleado_id>/', eliminar_empleado, name='eliminar_empleado'),
    path('edificio/reportes/', login_required(ReportesView.as_view()), name='reportes'),
     path('generar_excel/', generar_excel, name='generar_excel'),
    path('edificio/users/', login_required(UsersView.as_view()), name='users'),
    path('edificio/crearEmpleados/', login_required(EmpleadosCreateView.as_view()), name='crearEmpleados'),
    path('edificio/editarEmpleados/', login_required(EmpleadosEditView.as_view()), name='editarEmpleados'),
    path('edificio/createUsers/', login_required(UsersCreateView.as_view()), name='crearUsers'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cedula/',views.completarCedula)

]
