from django.contrib import admin
from django.urls import path, include
from . import views
from .views import equipment_list


urlpatterns = [
    path('equipment_list', equipment_list.as_view(), name="equipment_list"),
    path('equipment_details/<equip_id>', views.equipment_details, name="equipment_details"),

    
]
