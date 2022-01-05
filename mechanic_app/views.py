from django.shortcuts import render, redirect
from django.contrib import messages
from driver_app.models import VehicleInspectionReport
from django.views.generic import ListView, DetailView


def mechanic_area(request):
	return render(request, 'mechanic_app/mechanic_area.html', {})

class mech_report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'mechanic_app/mech_report_list.html'
	ordering = ['-date']

class mech_report_details(DetailView):
	model = VehicleInspectionReport
	template_name = 'mechanic_app/mech_report_details.html'