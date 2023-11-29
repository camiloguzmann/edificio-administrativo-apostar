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
from edificio_app import views
from edificio_app.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', (indexView.as_view()), name='index'),
    path('edificio/visitantes/',(CreateVisitanteFormView.as_view()), name='visitantes'),
    path('edificio/salida/',(VisitantesSalidaView.as_view()), name='salida'),
    path('obtener_datos_visitante/<int:cedula>/', ObtenerDatosVisitanteView.as_view(), name='obtener_datos_visitante'),
    path('salida/<int:visitante_id>/', SalidaView.as_view(), name='salida_visitante'),
    path('edificio/empleados/',(EmpleadoslistView.as_view()), name='empleados'),
    path('edificio/crearEmpleados/', (CreateEmpleadoFormView.as_view()), name='crearEmpleados'),
    path('editar_empleado/<int:empleado_id>/', EditarEmpleadoView.as_view(), name='editarEmpleados'),
    path('eliminar_empleado/<int:empleado_id>/', EliminarEmpleadoView.as_view(), name='eliminar_empleado'),
    path('edificio/reportes/',(ReportesView.as_view()), name='reportes'),
    path('generar_excel/', (GenerarExcelView.as_view()), name='generar_excel'),
    path('edificio/users/',(UsersListView.as_view()), name='users'),
    path('edificio/editarEmpleados/',(EmpleadosEditView.as_view()), name='editarEmpleados'),
    path('edificio/createUsers/',(UsersCreateView.as_view()), name='crearUsers'),
    path('editar_usuario/<int:usuario_id>/', (EditarUsuarioView.as_view()), name='editarUsuarios'),
    path('eliminar_usuario/<int:usuario_id>/', (EliminarUsuarioView.as_view()), name='eliminar_usuario'),
    path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cedula/',views.completarCedula)

]
