"""
Módulo de vistas para la app gestion_clinica.
Contiene las vistas tanto para templates HTML como para la API REST.
Incluye vistas para listar, crear, actualizar y eliminar registros.
Uso de comentarios explicativos en cada módulo o clase.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django_filters import rest_framework as filters

# Importación de filtros para la funcionalidad de búsqueda y filtrado
from .filters import (
    MedicoFilter, PacienteFilter, ConsultaMedicaFilter,
    TratamientoFilter, RecetaMedicaFilter, MedicamentoFilter
)
from django.http import HttpResponse   
from rest_framework import generics

# Importación de formularios para CRUD
from .forms import (
    PacienteForm, MedicoForm, EspecialidadForm, ConsultaMedicaForm,
    TratamientoForm, MedicamentoForm, RecetaMedicaForm
)

# Importación de modelos y serializadores
from .models import Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica
from .serializers import EspecialidadSerializer, PacienteSerializer, MedicoSerializer, ConsultaMedicaSerializer, TratamientoSerializer, MedicamentoSerializer, RecetaMedicaSerializer

def home(request):
    """
    Vista principal (home) del sistema Salud Vital.
    """
    return render(request, 'gestion_clinica/home.html')

def paciente_list_view(request):
    """
    Vista para listar pacientes con datos reales.
    """
    pacientes = Paciente.objects.all()
    return render(request, 'gestion_clinica/pacientes/list.html', {'pacientes': pacientes})

def medico_list_view(request):
    """
    Vista para listar médicos con datos reales.
    """
    medicos = Medico.objects.all()
    return render(request, 'gestion_clinica/medicos/list.html', {'medicos': medicos})

def consulta_list_view(request):
    """
    Vista para listar consultas con datos reales.
    """
    consultas = ConsultaMedica.objects.all()
    return render(request, 'gestion_clinica/consultas/list.html', {'consultas': consultas})

def especialidad_list_view(request):
    """
    Vista para listar especialidades con datos reales.
    """
    especialidades = Especialidad.objects.all()
    return render(request, 'gestion_clinica/especialidades/list.html', {'especialidades': especialidades})

def tratamiento_list_view(request):
    """
    Vista para listar tratamientos con datos reales.
    """
    tratamientos = Tratamiento.objects.all()
    return render(request, 'gestion_clinica/tratamientos/list.html', {'tratamientos': tratamientos})

def medicamento_list_view(request):
    """
    Vista para listar medicamentos con datos reales.
    """
    medicamentos = Medicamento.objects.all()
    return render(request, 'gestion_clinica/medicamentos/list.html', {'medicamentos': medicamentos})

def receta_list_view(request):
    """
    Vista para listar recetas con datos reales.
    """
    recetas = RecetaMedica.objects.all()
    return render(request, 'gestion_clinica/recetas/list.html', {'recetas': recetas})

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


# =============================================================================
# VISTAS CRUD PARA FORMULARIOS HTML
# =============================================================================

# CRUD PARA PACIENTES
def paciente_create_view(request):
    """
    Vista para crear un nuevo paciente mediante formulario HTML.
    """
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente creado exitosamente.')
            return redirect('paciente-list')
    else:
        form = PacienteForm()
    
    return render(request, 'gestion_clinica/pacientes/create.html', {'form': form})

def paciente_edit_view(request, id):
    """
    Vista para editar un paciente existente mediante formulario HTML.
    """
    paciente = get_object_or_404(Paciente, id=id)
    
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente actualizado exitosamente.')
            return redirect('paciente-list')
    else:
        form = PacienteForm(instance=paciente)
    
    return render(request, 'gestion_clinica/pacientes/edit.html', {'form': form, 'paciente': paciente})

def paciente_delete_view(request, id):
    """
    Vista para eliminar un paciente existente.
    """
    paciente = get_object_or_404(Paciente, id=id)
    
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente eliminado exitosamente.')
        return redirect('paciente-list')
    
    return render(request, 'gestion_clinica/pacientes/delete.html', {'paciente': paciente})


# CRUD PARA MÉDICOS
def medico_create_view(request):
    """
    Vista para crear un nuevo médico mediante formulario HTML.
    """
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico creado exitosamente.')
            return redirect('medico-list')
    else:
        form = MedicoForm()
    
    return render(request, 'gestion_clinica/medicos/create.html', {'form': form})

def medico_edit_view(request, id):
    """
    Vista para editar un médico existente mediante formulario HTML.
    """
    medico = get_object_or_404(Medico, id=id)
    
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico actualizado exitosamente.')
            return redirect('medico-list')
    else:
        form = MedicoForm(instance=medico)
    
    return render(request, 'gestion_clinica/medicos/edit.html', {'form': form, 'medico': medico})

def medico_delete_view(request, id):
    """
    Vista para eliminar un médico existente.
    """
    medico = get_object_or_404(Medico, id=id)
    
    if request.method == 'POST':
        medico.delete()
        messages.success(request, 'Médico eliminado exitosamente.')
        return redirect('medico-list')
    
    return render(request, 'gestion_clinica/medicos/delete.html', {'medico': medico})


# CRUD PARA ESPECIALIDADES
def especialidad_create_view(request):
    """
    Vista para crear una nueva especialidad mediante formulario HTML.
    """
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Especialidad creada exitosamente.')
            return redirect('especialidad-list')
    else:
        form = EspecialidadForm()
    
    return render(request, 'gestion_clinica/especialidades/create.html', {'form': form})

def especialidad_edit_view(request, id):
    """
    Vista para editar una especialidad existente mediante formulario HTML.
    """
    especialidad = get_object_or_404(Especialidad, id=id)
    
    if request.method == 'POST':
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Especialidad actualizada exitosamente.')
            return redirect('especialidad-list')
    else:
        form = EspecialidadForm(instance=especialidad)
    
    return render(request, 'gestion_clinica/especialidades/edit.html', {'form': form, 'especialidad': especialidad})

def especialidad_delete_view(request, id):
    """
    Vista para eliminar una especialidad existente.
    """
    especialidad = get_object_or_404(Especialidad, id=id)
    
    if request.method == 'POST':
        especialidad.delete()
        messages.success(request, 'Especialidad eliminada exitosamente.')
        return redirect('especialidad-list')
    
    return render(request, 'gestion_clinica/especialidades/delete.html', {'especialidad': especialidad})


# CRUD PARA CONSULTAS MÉDICAS
def consulta_create_view(request):
    """
    Vista para crear una nueva consulta médica mediante formulario HTML.
    """
    if request.method == 'POST':
        form = ConsultaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta médica creada exitosamente.')
            return redirect('consulta-list')
    else:
        form = ConsultaMedicaForm()
    
    return render(request, 'gestion_clinica/consultas/create.html', {'form': form})

def consulta_edit_view(request, id):
    """
    Vista para editar una consulta médica existente mediante formulario HTML.
    """
    consulta = get_object_or_404(ConsultaMedica, id=id)
    
    if request.method == 'POST':
        form = ConsultaMedicaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta médica actualizada exitosamente.')
            return redirect('consulta-list')
    else:
        form = ConsultaMedicaForm(instance=consulta)
    
    return render(request, 'gestion_clinica/consultas/edit.html', {'form': form, 'consulta': consulta})

def consulta_delete_view(request, id):
    """
    Vista para eliminar una consulta médica existente.
    """
    consulta = get_object_or_404(ConsultaMedica, id=id)
    
    if request.method == 'POST':
        consulta.delete()
        messages.success(request, 'Consulta médica eliminada exitosamente.')
        return redirect('consulta-list')
    
    return render(request, 'gestion_clinica/consultas/delete.html', {'consulta': consulta})


# CRUD PARA TRATAMIENTOS
def tratamiento_create_view(request):
    """
    Vista para crear un nuevo tratamiento mediante formulario HTML.
    """
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tratamiento creado exitosamente.')
            return redirect('tratamiento-list')
    else:
        form = TratamientoForm()
    
    return render(request, 'gestion_clinica/tratamientos/create.html', {'form': form})

def tratamiento_edit_view(request, id):
    """
    Vista para editar un tratamiento existente mediante formulario HTML.
    """
    tratamiento = get_object_or_404(Tratamiento, id=id)
    
    if request.method == 'POST':
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tratamiento actualizado exitosamente.')
            return redirect('tratamiento-list')
    else:
        form = TratamientoForm(instance=tratamiento)
    
    return render(request, 'gestion_clinica/tratamientos/edit.html', {'form': form, 'tratamiento': tratamiento})

def tratamiento_delete_view(request, id):
    """
    Vista para eliminar un tratamiento existente.
    """
    tratamiento = get_object_or_404(Tratamiento, id=id)
    
    if request.method == 'POST':
        tratamiento.delete()
        messages.success(request, 'Tratamiento eliminado exitosamente.')
        return redirect('tratamiento-list')
    
    return render(request, 'gestion_clinica/tratamientos/delete.html', {'tratamiento': tratamiento})


# CRUD PARA MEDICAMENTOS
def medicamento_create_view(request):
    """
    Vista para crear un nuevo medicamento mediante formulario HTML.
    """
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicamento creado exitosamente.')
            return redirect('medicamento-list')
    else:
        form = MedicamentoForm()
    
    return render(request, 'gestion_clinica/medicamentos/create.html', {'form': form})

def medicamento_edit_view(request, id):
    """
    Vista para editar un medicamento existente mediante formulario HTML.
    """
    medicamento = get_object_or_404(Medicamento, id=id)
    
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicamento actualizado exitosamente.')
            return redirect('medicamento-list')
    else:
        form = MedicamentoForm(instance=medicamento)
    
    return render(request, 'gestion_clinica/medicamentos/edit.html', {'form': form, 'medicamento': medicamento})

def medicamento_delete_view(request, id):
    """
    Vista para eliminar un medicamento existente.
    """
    medicamento = get_object_or_404(Medicamento, id=id)
    
    if request.method == 'POST':
        medicamento.delete()
        messages.success(request, 'Medicamento eliminado exitosamente.')
        return redirect('medicamento-list')
    
    return render(request, 'gestion_clinica/medicamentos/delete.html', {'medicamento': medicamento})


# CRUD PARA RECETAS MÉDICAS
def receta_create_view(request):
    """
    Vista para crear una nueva receta médica mediante formulario HTML.
    """
    if request.method == 'POST':
        form = RecetaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receta médica creada exitosamente.')
            return redirect('receta-list')
    else:
        form = RecetaMedicaForm()
    
    return render(request, 'gestion_clinica/recetas/create.html', {'form': form})

def receta_edit_view(request, id):
    """
    Vista para editar una receta médica existente mediante formulario HTML.
    """
    receta = get_object_or_404(RecetaMedica, id=id)
    
    if request.method == 'POST':
        form = RecetaMedicaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receta médica actualizada exitosamente.')
            return redirect('receta-list')
    else:
        form = RecetaMedicaForm(instance=receta)
    
    return render(request, 'gestion_clinica/recetas/edit.html', {'form': form, 'receta': receta})

def receta_delete_view(request, id):
    """
    Vista para eliminar una receta médica existente.
    """
    receta = get_object_or_404(RecetaMedica, id=id)
    
    if request.method == 'POST':
        receta.delete()
        messages.success(request, 'Receta médica eliminada exitosamente.')
        return redirect('receta-list')
    
    return render(request, 'gestion_clinica/recetas/delete.html', {'receta': receta})