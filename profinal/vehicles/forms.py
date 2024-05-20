# vehicles/forms.py
from django import forms
from .models import DriverVehicle

class DriverVehicleForm(forms.ModelForm):
    class Meta:
        model = DriverVehicle
        fields = [
            # Añade el campo user al formulario
            'num_placa', 'modelo', 'ano', 'estado', 'tipo',
            'num_licencia', 'tipo_licencia'
        ]

