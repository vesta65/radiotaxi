# vehicles/urls.py
from django.urls import path
from .views import create_driver_vehicle, vehicle_list, vehicle_edit, vehicle_delete

urlpatterns = [
    path('create_driver_vehicle/', create_driver_vehicle, name='create_driver_vehicle'),
    path('vehicles/', vehicle_list, name='vehicle_list'),
    path('vehicles/<int:vehicle_id>/edit/', vehicle_edit, name='vehicle_edit'),
    path('vehicles/<int:vehicle_id>/delete/', vehicle_delete, name='vehicle_delete'),  # URL para la eliminación del vehículo
]
