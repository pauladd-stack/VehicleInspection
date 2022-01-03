from django.contrib import admin
from django.urls import path, include
from . import views
from .views import mech_report_list, mech_report_details

urlpatterns = [
path('mechanic_area', views.mechanic_area, name="mechanic_area"),
path('mech_report_list', mech_report_list.as_view(), name="mech_report_list"),
path('mech_report_details/<int:pk>', mech_report_details.as_view(), name="mech_report_details"),
]
