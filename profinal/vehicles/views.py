# vehicles/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DriverVehicleForm
from .models import DriverVehicle

@login_required
def create_driver_vehicle(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirigir al usuario a la página de inicio de sesión si no está autenticado

    if request.user.edad is None or request.user.edad < 18:
        return redirect('home')  # Redirigir si el usuario no tiene una edad válida

    if request.method == 'POST':
        form = DriverVehicleForm(request.POST)
        if form.is_valid():
            driver_vehicle = form.save(commit=False)
            driver_vehicle.user = request.user  # Asignar el usuario automáticamente
            driver_vehicle.save()
            return redirect('home')  # Redirigir a la página principal o a donde prefieras
    else:
        form = DriverVehicleForm(initial={'user': request.user})  # Establecer el usuario inicialmente

    return render(request, 'vehicles/register.html', {'form': form})

def vehicle_list(request):
    vehicles = DriverVehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

def vehicle_edit(request, vehicle_id):
    vehicle = get_object_or_404(DriverVehicle, pk=vehicle_id)
    if request.method == 'POST':
        form = DriverVehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')  # Redirigir a la lista de vehículos después de editar
    else:
        form = DriverVehicleForm(instance=vehicle)
    return render(request, 'vehicles/vehicle_edit.html', {'form': form})

def vehicle_delete(request, vehicle_id):
    vehicle = get_object_or_404(DriverVehicle, pk=vehicle_id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')  # Redirigir a la lista de vehículos después de eliminar
    return render(request, 'vehicles/vehicle_confirm_delete.html', {'vehicle': vehicle})
