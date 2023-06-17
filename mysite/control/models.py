from django.db import models
from django.utils import timezone

class Empleado(models.Model):
    TURNOS_CHOICES = (
        ('D', 'Día'),
        ('T', 'Tarde'),
        ('N', 'Noche'),
    )

    nombre = models.CharField(max_length=150)
    departamento = models.CharField(max_length=100)
    fecha_inicio = models.DateField(default=timezone.now)
    dias_trabajo = models.CharField(max_length=100)
    turno = models.CharField(max_length=1, choices=TURNOS_CHOICES)
    horario_entrada = models.TimeField()
    horario_salida = models.TimeField()



class Jornada(models.Model):
    TIPO_MARCACION_CHOICES = (
        ('E', 'Entrada'),
        ('S', 'Salida'),
    )

    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    tipo_marcacion = models.CharField(max_length=1, choices=TIPO_MARCACION_CHOICES)
