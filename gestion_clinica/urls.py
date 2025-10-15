"""
Módulo de URLs para la app gestion_clinica.
Define las rutas tanto para templates HTML como para endpoints de la API REST.
Incluye rutas para operaciones CRUD (Create, Read, Update, Delete) de todas las entidades.
Permite el acceso a la funcionalidad del sistema desde diferentes interfaces.
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
    home, paciente_list_view, medico_list_view, consulta_list_view,
    especialidad_list_view, tratamiento_list_view, medicamento_list_view, receta_list_view,
    # Vistas CRUD para formularios HTML
    paciente_create_view, paciente_edit_view, paciente_delete_view,
    medico_create_view, medico_edit_view, medico_delete_view,
    especialidad_create_view, especialidad_edit_view, especialidad_delete_view,
    consulta_create_view, consulta_edit_view, consulta_delete_view,
    tratamiento_create_view, tratamiento_edit_view, tratamiento_delete_view,
    medicamento_create_view, medicamento_edit_view, medicamento_delete_view,
    receta_create_view, receta_edit_view, receta_delete_view
)

urlpatterns = [
    # Rutas para templates HTML (vistas web)
    path('web/especialidades/', especialidad_list_view, name='especialidad-list'),
    path('web/pacientes/', paciente_list_view, name='paciente-list'),
    path('web/medicos/', medico_list_view, name='medico-list'),
    path('web/consultas/', consulta_list_view, name='consulta-list'),
    path('web/tratamientos/', tratamiento_list_view, name='tratamiento-list'),
    path('web/medicamentos/', medicamento_list_view, name='medicamento-list'),
    path('web/recetas/', receta_list_view, name='receta-list'),
    
    # =============================================================================
    # RUTAS CRUD PARA FORMULARIOS HTML
    # =============================================================================
    
    # CRUD para Pacientes
    path('web/pacientes/crear/', paciente_create_view, name='paciente-create'),
    path('web/pacientes/editar/<int:id>/', paciente_edit_view, name='paciente-edit'),
    path('web/pacientes/eliminar/<int:id>/', paciente_delete_view, name='paciente-delete'),
    
    # CRUD para Médicos
    path('web/medicos/crear/', medico_create_view, name='medico-create'),
    path('web/medicos/editar/<int:id>/', medico_edit_view, name='medico-edit'),
    path('web/medicos/eliminar/<int:id>/', medico_delete_view, name='medico-delete'),
    
    # CRUD para Especialidades
    path('web/especialidades/crear/', especialidad_create_view, name='especialidad-create'),
    path('web/especialidades/editar/<int:id>/', especialidad_edit_view, name='especialidad-edit'),
    path('web/especialidades/eliminar/<int:id>/', especialidad_delete_view, name='especialidad-delete'),
    
    # CRUD para Consultas Médicas
    path('web/consultas/crear/', consulta_create_view, name='consulta-create'),
    path('web/consultas/editar/<int:id>/', consulta_edit_view, name='consulta-edit'),
    path('web/consultas/eliminar/<int:id>/', consulta_delete_view, name='consulta-delete'),
    
    # CRUD para Tratamientos
    path('web/tratamientos/crear/', tratamiento_create_view, name='tratamiento-create'),
    path('web/tratamientos/editar/<int:id>/', tratamiento_edit_view, name='tratamiento-edit'),
    path('web/tratamientos/eliminar/<int:id>/', tratamiento_delete_view, name='tratamiento-delete'),
    
    # CRUD para Medicamentos
    path('web/medicamentos/crear/', medicamento_create_view, name='medicamento-create'),
    path('web/medicamentos/editar/<int:id>/', medicamento_edit_view, name='medicamento-edit'),
    path('web/medicamentos/eliminar/<int:id>/', medicamento_delete_view, name='medicamento-delete'),
    
    # CRUD para Recetas Médicas
    path('web/recetas/crear/', receta_create_view, name='receta-create'),
    path('web/recetas/editar/<int:id>/', receta_edit_view, name='receta-edit'),
    path('web/recetas/eliminar/<int:id>/', receta_delete_view, name='receta-delete'),
    
    # Endpoints API REST para especialidades
    path('especialidades/', EspecialidadListCreateView.as_view(), name='especialidad-list-create'),
    path('especialidades/<int:pk>/', EspecialidadRetrieveUpdateDestroyView.as_view(), name='especialidad-detail'),

    # Endpoints API REST para pacientes
    path('pacientes/', PacienteListCreateView.as_view(), name='paciente-list-create'),
    path('pacientes/<int:pk>/', PacienteRetrieveUpdateDestroyView.as_view(), name='paciente-detail'),

    # Endpoints API REST para médicos
    path('medicos/', MedicoListCreateView.as_view(), name='medico-list-create'),
    path('medicos/<int:pk>/', MedicoRetrieveUpdateDestroyView.as_view(), name='medico-detail'),

    # Endpoints API REST para consultas médicas
    path('consultas/', ConsultaMedicaListCreateView.as_view(), name='consulta-list-create'),
    path('consultas/<int:pk>/', ConsultaMedicaRetrieveUpdateDestroyView.as_view(), name='consulta-detail'),

    # Endpoints API REST para tratamientos
    path('tratamientos/', TratamientoListCreateView.as_view(), name='tratamiento-list-create'),
    path('tratamientos/<int:pk>/', TratamientoRetrieveUpdateDestroyView.as_view(), name='tratamiento-detail'),

    # Endpoints API REST para medicamentos
    path('medicamentos/', MedicamentoListCreateView.as_view(), name='medicamento-list-create'),
    path('medicamentos/<int:pk>/', MedicamentoRetrieveUpdateDestroyView.as_view(), name='medicamento-detail'),
    
    # Endpoints API REST para recetas médicas
    path('recetas/', RecetaMedicaListCreateView.as_view(), name='receta-list-create'),
    path('recetas/<int:pk>/', RecetaMedicaRetrieveUpdateDestroyView.as_view(), name='receta-detail'),
]

