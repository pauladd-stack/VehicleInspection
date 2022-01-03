from django.contrib import admin
from django.urls import path, include
from . import views
from .views import report_list, report_details

urlpatterns = [    
path('driver_area', views.driver_area, name="driver_area"),
path('inspection_report', views.inspection_report, name="inspection_report"),
path('report_list', report_list.as_view(), name="report_list"),
path('report_details/<int:pk>', report_details.as_view(), name="report_details"),


]
