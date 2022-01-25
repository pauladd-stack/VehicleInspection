from django.contrib import admin
from django.urls import path, include
from . import views
from .views import report_list, completed_driver_report_list

urlpatterns = [    
path('driver_area', views.driver_area, name="driver_area"),
path('inspection_report', views.inspection_report, name="inspection_report"),
path('report_list', report_list.as_view(), name="report_list"),
path('driver_report_details/<report_id>', views.driver_report_details, name="driver_report_details"),
path('completed_driver_report_list', completed_driver_report_list.as_view(), name="completed_driver_report_list"),



]
