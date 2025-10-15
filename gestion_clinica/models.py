"""
Modelos de datos para la app gestion_clinica.
Incluye las entidades principales del sistema clínico.
"""
from django.db import models

class Especialidad(models.Model):
    """
    Modelo para representar especialidades médicas.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    """
    Modelo para representar pacientes.
    Incluye CHOICES para tipo de sangre.
    """
    # Definición de CHOICES para tipo de sangre
    TIPO_SANGRE_CHOICES = [
        ('A+', 'A positivo'),
        ('A-', 'A negativo'),
        ('B+', 'B positivo'),
        ('B-', 'B negativo'),
        ('AB+', 'AB positivo'),
        ('AB-', 'AB negativo'),
        ('O+', 'O positivo'),
        ('O-', 'O negativo'),
    ]

    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    tipo_sangre = models.CharField(
        max_length=3,
        choices=TIPO_SANGRE_CHOICES,
        default='O+'
    )
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Medico(models.Model):
    """
    Modelo para representar médicos.
    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"

class ConsultaMedica(models.Model):
    """
    Modelo para representar consultas médicas.
    Incluye CHOICES para estado de la consulta.
    """
    # Definición de CHOICES para estado de consulta
    ESTADO_CHOICES = [
        ('AGENDADA', 'Agendada'),
        ('EN_CURSO', 'En Curso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
        ('NO_ASISTIO', 'No Asistió'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_consulta = models.DateTimeField()
    motivo = models.CharField(max_length=200)
    diagnostico = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='AGENDADA'
    )

    def __str__(self):
        return f"Consulta de {self.paciente} con {self.medico}"

class Tratamiento(models.Model):
    """
    Modelo para representar tratamientos médicos.
    """
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    descripcion = models.TextField()
    duracion_dias = models.IntegerField()
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Tratamiento para {self.consulta.paciente}"

class Medicamento(models.Model):
    """
    Modelo para representar medicamentos.
    """
    nombre = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class RecetaMedica(models.Model):
    """
    Modelo para representar recetas médicas.
    Incluye CHOICES para frecuencia de medicación.
    """
    # Definición de CHOICES para frecuencia de medicación
    FRECUENCIA_CHOICES = [
        ('8H', 'Cada 8 horas'),
        ('12H', 'Cada 12 horas'),
        ('24H', 'Cada 24 horas'),
        ('48H', 'Cada 48 horas'),
        ('SEMANAL', 'Una vez por semana'),
        ('UNICA', 'Dosis única'),
    ]

    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(
        max_length=10,
        choices=FRECUENCIA_CHOICES,
        default='24H'
    )
    duracion = models.CharField(max_length=100)
    motivo = models.CharField(max_length=200)

    def __str__(self):
        return f"Receta de {self.medicamento} para {self.tratamiento.consulta.paciente}"