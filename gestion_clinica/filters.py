"""
Filtros personalizados para los modelos de la aplicación.
Permite filtrar los registros según diferentes criterios.
"""
from django_filters import rest_framework as filters
from .models import Medico, Paciente, ConsultaMedica, Tratamiento, RecetaMedica, Medicamento

class MedicoFilter(filters.FilterSet):
    """
    Filtros para el modelo Médico.
    Permite filtrar médicos por especialidad y estado activo.
    """
    especialidad = filters.NumberFilter(field_name='especialidad__id')
    especialidad_nombre = filters.CharFilter(field_name='especialidad__nombre', lookup_expr='icontains')
    activo = filters.BooleanFilter()

    class Meta:
        model = Medico
        fields = ['especialidad', 'especialidad_nombre', 'activo']

class PacienteFilter(filters.FilterSet):
    """
    Filtros para el modelo Paciente.
    Permite filtrar pacientes por médico tratante y tipo de sangre.
    """
    medico = filters.NumberFilter(field_name='consultamedica__medico__id', distinct=True)
    tipo_sangre = filters.ChoiceFilter(choices=Paciente.TIPO_SANGRE_CHOICES)
    activo = filters.BooleanFilter()

    class Meta:
        model = Paciente
        fields = ['medico', 'tipo_sangre', 'activo']

class ConsultaMedicaFilter(filters.FilterSet):
    """
    Filtros para el modelo ConsultaMedica.
    Permite filtrar consultas por médico, paciente, estado y rango de fechas.
    """
    medico = filters.NumberFilter(field_name='medico__id')
    paciente = filters.NumberFilter(field_name='paciente__id')
    estado = filters.ChoiceFilter(choices=ConsultaMedica.ESTADO_CHOICES)
    fecha_desde = filters.DateTimeFilter(field_name='fecha_consulta', lookup_expr='gte')
    fecha_hasta = filters.DateTimeFilter(field_name='fecha_consulta', lookup_expr='lte')

    class Meta:
        model = ConsultaMedica
        fields = ['medico', 'paciente', 'estado', 'fecha_desde', 'fecha_hasta']

class TratamientoFilter(filters.FilterSet):
    """
    Filtros para el modelo Tratamiento.
    Permite filtrar tratamientos por consulta y médico.
    """
    consulta = filters.NumberFilter(field_name='consulta__id')
    medico = filters.NumberFilter(field_name='consulta__medico__id')
    paciente = filters.NumberFilter(field_name='consulta__paciente__id')

    class Meta:
        model = Tratamiento
        fields = ['consulta', 'medico', 'paciente']

class RecetaMedicaFilter(filters.FilterSet):
    """
    Filtros para el modelo RecetaMedica.
    Permite filtrar recetas por tratamiento, medicamento y frecuencia.
    """
    tratamiento = filters.NumberFilter(field_name='tratamiento__id')
    medicamento = filters.NumberFilter(field_name='medicamento__id')
    frecuencia = filters.ChoiceFilter(choices=RecetaMedica.FRECUENCIA_CHOICES)

    class Meta:
        model = RecetaMedica
        fields = ['tratamiento', 'medicamento', 'frecuencia']

class MedicamentoFilter(filters.FilterSet):
    """
    Filtros para el modelo Medicamento.
    Permite filtrar medicamentos por nombre y laboratorio.
    """
    nombre = filters.CharFilter(lookup_expr='icontains')
    laboratorio = filters.CharFilter(lookup_expr='icontains')
    stock_minimo = filters.NumberFilter(field_name='stock', lookup_expr='gte')

    class Meta:
        model = Medicamento
        fields = ['nombre', 'laboratorio', 'stock_minimo']