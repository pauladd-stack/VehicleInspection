from django.contrib import admin
from django.urls import path, include
from . import views
from .views import mech_report_list, completed_mech_report_list

urlpatterns = [
path('mech_report_list', mech_report_list.as_view(), name="mech_report_list"),
path('completed_mech_report_list', completed_mech_report_list.as_view(), name="completed_mech_report_list"),
path('mechanic_report_details/<report_id>', views.mechanic_report_details, name="mechanic_report_details"),
path('completed_mechanic_report_details/<report_id>', views.completed_mechanic_report_details, name="completed_mechanic_report_details"),

]
