"""
URL configuration for saludvital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
"""
Módulo de URLs principal del proyecto Salud Vital.
Define las rutas base y la integración de las apps.
Uso de comentarios explicativos en cada módulo o clase.
"""

from django.contrib import admin
from django.urls import path, include
from gestion_clinica.views import home

# Inclusión de las rutas de la app gestion_clinica
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('gestion_clinica.urls')),
]


