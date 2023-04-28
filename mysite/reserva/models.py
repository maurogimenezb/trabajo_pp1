from django.db import models

class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    num_huespedes = models.PositiveIntegerField()
    tipo_habitacion = models.CharField(max_length=50)
    precio_total = models.DecimalField(max_digits=8, decimal_places=2)
    ESTADO_CHOICES = (
        ('C', 'Confirmada'),
        ('P', 'Pendiente'),
        ('X', 'Cancelada')
    )
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES)

    def __str__(self):
        return f"Reserva en {self.hotel} para {self.num_huespedes} huespedes del {self.fecha_entrada} al {self.fecha_salida}"
