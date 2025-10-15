"""
Formularios para el CRUD de todas las entidades del sistema Salud Vital.
Permite crear, editar y validar datos de pacientes, médicos, especialidades, etc.
"""

from django import forms
from .models import (
    Paciente, Medico, Especialidad, ConsultaMedica, 
    Tratamiento, Medicamento, RecetaMedica
)


class PacienteForm(forms.ModelForm):
    """
    Formulario para crear y editar pacientes.
    Incluye validaciones para RUT y datos personales.
    """
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'rut', 'fecha_nacimiento', 'telefono', 'correo', 'direccion', 'tipo_sangre']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'telefono': forms.TextInput(attrs={'placeholder': '+56 9 1234 5678'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
            'direccion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Dirección completa del paciente'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'rut': 'RUT (sin puntos ni guión)',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'telefono': 'Teléfono',
            'correo': 'Correo Electrónico',
            'direccion': 'Dirección',
            'tipo_sangre': 'Tipo de Sangre',
        }


class MedicoForm(forms.ModelForm):
    """
    Formulario para crear y editar médicos.
    Incluye selección de especialidad y validaciones.
    """
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'rut', 'especialidad', 'telefono', 'correo']
        widgets = {
            'telefono': forms.TextInput(attrs={'placeholder': '+56 9 1234 5678'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'rut': 'RUT (sin puntos ni guión)',
            'especialidad': 'Especialidad',
            'telefono': 'Teléfono',
            'correo': 'Correo Electrónico',
        }


class EspecialidadForm(forms.ModelForm):
    """
    Formulario para crear y editar especialidades médicas.
    """
    class Meta:
        model = Especialidad
        fields = ['nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descripción detallada de la especialidad'}),
        }
        labels = {
            'nombre': 'Nombre de la Especialidad',
            'descripcion': 'Descripción',
        }


class ConsultaMedicaForm(forms.ModelForm):
    """
    Formulario para crear y editar consultas médicas.
    Incluye selección de paciente y médico.
    """
    class Meta:
        model = ConsultaMedica
        fields = ['paciente', 'medico', 'fecha_consulta', 'motivo', 'diagnostico', 'estado']
        widgets = {
            'fecha_consulta': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'motivo': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Motivo de la consulta'}),
            'diagnostico': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Diagnóstico médico'}),
        }
        labels = {
            'paciente': 'Paciente',
            'medico': 'Médico',
            'fecha_consulta': 'Fecha y Hora de Consulta',
            'motivo': 'Motivo de la Consulta',
            'diagnostico': 'Diagnóstico',
            'estado': 'Estado de la Consulta',
        }


class TratamientoForm(forms.ModelForm):
    """
    Formulario para crear y editar tratamientos médicos.
    """
    class Meta:
        model = Tratamiento
        fields = ['consulta', 'descripcion', 'duracion_dias', 'observaciones']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descripción detallada del tratamiento'}),
            'observaciones': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Observaciones adicionales'}),
        }
        labels = {
            'consulta': 'Consulta Médica',
            'descripcion': 'Descripción del Tratamiento',
            'duracion_dias': 'Duración en Días',
            'observaciones': 'Observaciones',
        }


class MedicamentoForm(forms.ModelForm):
    """
    Formulario para crear y editar medicamentos.
    Incluye validaciones para stock y precios.
    """
    class Meta:
        model = Medicamento
        fields = ['nombre', 'laboratorio', 'stock', 'precio_unitario']
        widgets = {
            'stock': forms.NumberInput(attrs={'min': '0', 'placeholder': 'Cantidad en stock'}),
            'precio_unitario': forms.NumberInput(attrs={'min': '0', 'step': '0.01', 'placeholder': '0.00'}),
        }
        labels = {
            'nombre': 'Nombre del Medicamento',
            'laboratorio': 'Laboratorio',
            'stock': 'Stock Disponible',
            'precio_unitario': 'Precio Unitario ($)',
        }


class RecetaMedicaForm(forms.ModelForm):
    """
    Formulario para crear y editar recetas médicas.
    Incluye selección de tratamiento y medicamento.
    """
    class Meta:
        model = RecetaMedica
        fields = ['tratamiento', 'medicamento', 'dosis', 'frecuencia', 'duracion', 'motivo']
        widgets = {
            'dosis': forms.TextInput(attrs={'placeholder': 'Ej: 500mg, 1 comprimido'}),
            'duracion': forms.TextInput(attrs={'placeholder': 'Ej: 7 días, 2 semanas'}),
            'motivo': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Motivo de la prescripción'}),
        }
        labels = {
            'tratamiento': 'Tratamiento',
            'medicamento': 'Medicamento',
            'dosis': 'Dosis',
            'frecuencia': 'Frecuencia',
            'duracion': 'Duración',
            'motivo': 'Motivo de la Prescripción',
        }
