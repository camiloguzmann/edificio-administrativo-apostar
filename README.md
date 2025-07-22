# Edificio Administrativo Apostar

Este proyecto es una aplicación web desarrollada con Django para la gestión administrativa de un edificio. Permite la administración de usuarios, empleados y visitantes, así como la generación de reportes y control de accesos.

## Características principales
- Gestión de usuarios y roles (administrador, empleados, visitantes)
- Registro y control de acceso de visitantes
- Administración de empleados
- Generación de reportes
- Interfaz web moderna y responsiva

## Tecnologías utilizadas
- Python 3
- Django 4.2.4
- SQLite (por defecto, configurable a otros motores)
- HTML, CSS, JavaScript (frontend)
- Librerías adicionales: django-crispy-forms, openpyxl, opencv-python, spacy, entre otras (ver `requirements.txt`)

## Estructura del proyecto
```
edificio-administrativo-apostar/
├── edificio_administrativo/   # Configuración principal Django
├── edificio_app/              # Lógica de la aplicación
├── static/                    # Archivos estáticos (CSS, JS, imágenes)
├── templates/                 # Plantillas HTML
├── db.sqlite3                 # Base de datos SQLite (por defecto)
├── manage.py                  # Script de gestión Django
├── requirements.txt           # Dependencias del proyecto
```

## Instalación y ejecución
1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd edificio-administrativo-apostar
   ```
2. Crea un entorno virtual e instala dependencias:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   pip install -r requirements.txt
   ```
3. Realiza las migraciones y ejecuta el servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
4. Accede a la aplicación en [http://localhost:8000](http://localhost:8000)

## Personalización
- Para cambiar la base de datos o configuraciones, edita `edificio_administrativo/settings.py`.
- Las plantillas HTML están en la carpeta `templates/`.
- Los archivos estáticos (CSS, JS, imágenes) están en `static/`.

## Autor
- Desarrollado por: Camilo Guzman Salgado 

---
¡Contribuciones y sugerencias son bienvenidas!
