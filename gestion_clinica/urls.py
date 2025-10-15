"""
Archivo de rutas para la app gestion_clinica.
Define los endpoints para el CRUD de Especialidad.
Uso de comentarios explicativos en cada módulo o clase.
"""
from django.urls import path
from .views import (
    EspecialidadListCreateView, EspecialidadRetrieveUpdateDestroyView,
    PacienteListCreateView, PacienteRetrieveUpdateDestroyView,
    MedicoListCreateView, MedicoRetrieveUpdateDestroyView,
    ConsultaMedicaListCreateView, ConsultaMedicaRetrieveUpdateDestroyView,
    TratamientoListCreateView, TratamientoRetrieveUpdateDestroyView,
    MedicamentoListCreateView, MedicamentoRetrieveUpdateDestroyView,
    RecetaMedicaListCreateView, RecetaMedicaRetrieveUpdateDestroyView,
    home
)

urlpatterns = [
    # Endpoint para listar y crear especialidades
    path('especialidades/', EspecialidadListCreateView.as_view(), name='especialidad-list-create'),
    # Endpoint para obtener, actualizar y eliminar una especialidad específica
    path('especialidades/<int:pk>/', EspecialidadRetrieveUpdateDestroyView.as_view(), name='especialidad-detail'),

    # Endpoint para listar y crear pacientes
    path('pacientes/', PacienteListCreateView.as_view(), name='paciente-list-create'),
    # Endpoint para obtener, actualizar y eliminar un paciente específico
    path('pacientes/<int:pk>/', PacienteRetrieveUpdateDestroyView.as_view(), name='paciente-detail'),

    # Endpoint para listar y crear médicos
    path('medicos/', MedicoListCreateView.as_view(), name='medico-list-create'),
    # Endpoint para obtener, actualizar y eliminar un médico específico
    path('medicos/<int:pk>/', MedicoRetrieveUpdateDestroyView.as_view(), name='medico-detail'),

    # Endpoint para listar y crear consultas médicas
    path('consultas/', ConsultaMedicaListCreateView.as_view(), name='consulta-list-create'),
    # Endpoint para obtener, actualizar y eliminar una consulta médica específica
    path('consultas/<int:pk>/', ConsultaMedicaRetrieveUpdateDestroyView.as_view(), name='consulta-detail'),

    # Endpoint para listar y crear tratamientos
    path('tratamientos/', TratamientoListCreateView.as_view(), name='tratamiento-list-create'),
    # Endpoint para obtener, actualizar y eliminar un tratamiento específico
    path('tratamientos/<int:pk>/', TratamientoRetrieveUpdateDestroyView.as_view(), name='tratamiento-detail'),

    # Endpoint para listar y crear medicamentos
    path('medicamentos/', MedicamentoListCreateView.as_view(), name='medicamento-list-create'),
    # Endpoint para obtener, actualizar y eliminar un medicamento específico
    path('medicamentos/<int:pk>/', MedicamentoRetrieveUpdateDestroyView.as_view(), name='medicamento-detail'),
    
    # Endpoint para listar y crear recetas médicas
    path('recetas/', RecetaMedicaListCreateView.as_view(), name='receta-list-create'),
    # Endpoint para obtener, actualizar y eliminar una receta médica específica
    path('recetas/<int:pk>/', RecetaMedicaRetrieveUpdateDestroyView.as_view(), name='receta-detail'),
]

