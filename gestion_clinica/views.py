"""
Vistas de la app gestion_clinica.
Gestiona la lógica de presentación y acceso a los datos.
Uso de comentarios explicativos en cada módulo o clase.
"""

from django.shortcuts import render
from django_filters import rest_framework as filters

# Crea las nuevas vistas aqui
from .filters import (
    MedicoFilter, PacienteFilter, ConsultaMedicaFilter,
    TratamientoFilter, RecetaMedicaFilter, MedicamentoFilter
)
from django.http import HttpResponse   
from rest_framework import generics
from .models import Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica
from .serializers import EspecialidadSerializer, PacienteSerializer, MedicoSerializer, ConsultaMedicaSerializer, TratamientoSerializer, MedicamentoSerializer, RecetaMedicaSerializer

def home(request):
    """
    Vista principal (home) del sistema Salud Vital.
    """
    return HttpResponse("<h1>Bienvenido al sistema Salud Vital</h1>")

# Vista para listar y crear especialidades
class EspecialidadListCreateView(generics.ListCreateAPIView):
    """
    Permite listar todas las especialidades y crear una nueva.
    """
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

# Vista para obtener, actualizar y eliminar una especialidad
class EspecialidadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Permite obtener, actualizar o eliminar una especialidad específica.
    """
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

# Vista para listar y crear pacientes
class PacienteListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar todos los pacientes y crear nuevos.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filterset_class = PacienteFilter 

# Vista para ver, actualizar o eliminar un paciente específico
class PacienteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver, actualizar o eliminar un paciente específico.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar todos los médicos y crear nuevos.
    Incluye la relación con su especialidad.
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filterset_class = MedicoFilter  

class MedicoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver, actualizar o eliminar un médico específico.
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


class ConsultaMedicaListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar todas las consultas médicas y crear nuevas.
    Incluye las relaciones con paciente y médico.
    """
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer
    filterset_class = ConsultaMedicaFilter

class ConsultaMedicaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver, actualizar o eliminar una consulta médica específica.
    """
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class TratamientoListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar todos los tratamientos y crear nuevos.
    Incluye la relación con la consulta médica.
    """
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer
    filterset_class = TratamientoFilter

class TratamientoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver, actualizar o eliminar un tratamiento específico.
    """
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class MedicamentoListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar todos los medicamentos y crear nuevos.
    """
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    filterset_class = MedicamentoFilter  

class MedicamentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver, actualizar o eliminar un medicamento específico.
    """
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class RecetaMedicaListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar todas las recetas médicas y crear nuevas.
    Incluye las relaciones con tratamiento y medicamento.
    """
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer
    filterset_class = RecetaMedicaFilter

class RecetaMedicaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver, actualizar o eliminar una receta médica específica.
    """
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer