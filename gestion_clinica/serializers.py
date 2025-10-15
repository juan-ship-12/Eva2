"""
Serializador para el modelo Especialidad.
Convierte instancias de Especialidad a JSON y viceversa.
Uso de comentarios explicativos en cada módulo o clase.
"""
from rest_framework import serializers
from .models import Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica

class EspecialidadSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Especialidad.
    """
    class Meta:
        model = Especialidad
        fields = '__all__'

# Serializador para el modelo Paciente
class PacienteSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Paciente.
    Incluye todos los campos del modelo y sus validaciones.
    """
    class Meta:
        model = Paciente
        fields = '__all__'

# Serializador para el modelo Medico
class MedicoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Médico.
    Incluye la relación con Especialidad y todos los campos del modelo.
    """
    class Meta:
        model = Medico
        fields = '__all__'

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo ConsultaMedica.
    Incluye las relaciones con Paciente y Médico.
    """
    class Meta:
        model = ConsultaMedica
        fields = '__all__'

# Serializador para el modelo Tratamiento
class TratamientoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Tratamiento.
    Incluye la relación con ConsultaMedica.
    """
    class Meta:
        model = Tratamiento
        fields = '__all__'

# Serializador para el modelo Medicamento
class MedicamentoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Medicamento.
    """
    class Meta:
        model = Medicamento
        fields = '__all__'

# Serializador para el modelo RecetaMedica
class RecetaMedicaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo RecetaMedica.
    Incluye las relaciones con Tratamiento y Medicamento.
    """
    class Meta:
        model = RecetaMedica
        fields = '__all__'