# vehicles/models.py
from django.db import models
from accounts.models import CustomUser

class DriverVehicle(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    num_placa = models.CharField(max_length=20, unique=True)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    TIPO_CHOICES = [
        ('taxi', 'taxi'),
        ('camioneta', 'camioneta'),
        ('trufi', 'trufi'),
        ('moto', 'moto'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    num_licencia = models.CharField(max_length=20, unique=True)
    tipo_licencia = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.num_placa} - {self.user.username}'
