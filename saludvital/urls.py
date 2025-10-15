"""
Módulo de URLs principal del proyecto Salud Vital.
Configura las rutas principales del sistema de gestión clínica.
Incluye integración con Django Admin, API REST, documentación Swagger y templates.
Permite el acceso a todas las funcionalidades del sistema desde diferentes interfaces.
Uso de comentarios explicativos en cada módulo o clase.
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from gestion_clinica.views import home

# Configuración de Swagger/OpenAPI
schema_view = get_schema_view(
   openapi.Info(
      title="Salud Vital API",
      default_version='v1',
      description="API para el sistema de gestión clínica Salud Vital",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@saludvital.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Inclusión de las rutas de la app gestion_clinica
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('gestion_clinica.urls')),
    
    # URLs para el browsable API y documentación
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]


