from django.shortcuts import render, redirect
from .forms import VehicleInspectionForm
from .models import VehicleInspectionReport
from django.contrib import messages
from django.views.generic import ListView, DetailView


def driver_area(request):
	return render(request, 'driver_app/driver_area.html', {})

def inspection_report(request):
	if request.method == "POST":
		form = VehicleInspectionForm(request.POST)
		if form.is_valid():
			driver = form.save(commit=False)
			driver.driver = request.user
			driver.save()
			messages.success(request, 'Submitted')
			return redirect('inspection_report')
		else:
			messages.error(request, 'Please correct the error below.')
			
	else:
		form = VehicleInspectionForm()

	return render(request, 'driver_app/inspection_report.html', {
		'form': form,
		})

class report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'driver_app/report_list.html'

class report_details(DetailView):
	model = VehicleInspectionReport
	template_name = 'driver_app/report_details.html'