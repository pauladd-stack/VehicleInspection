from django.shortcuts import render, redirect
from .forms import VehicleInspectionForm
from .models import VehicleInspectionReport
from django.contrib import messages
from django.views.generic import ListView, DetailView
import datetime
from vehicle_website.wraps import driver_only
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
@driver_only
def driver_area(request):
	obj = VehicleInspectionReport.history.all()
	return render(request, 'driver_app/driver_area.html', {'object': obj})

@login_required
@driver_only
def inspection_report(request):
	if request.method == "POST":
		form = VehicleInspectionForm(request.POST)
		if form.is_valid():
			driver = form.save(commit=False)
			driver.driver = request.user
			driver.lastUpdatedUser = datetime.datetime.now()
			driver._change_reason = 'Driver created a new ticket'
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


@method_decorator(login_required, name='dispatch')
@method_decorator(driver_only, name='dispatch')
class report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'driver_app/report_list.html'
	ordering = ['-date']


@method_decorator(login_required, name='dispatch')
@method_decorator(driver_only, name='dispatch')
class completed_driver_report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'driver_app/completed_driver_report_list.html'
	ordering = ['-date']


@login_required
@driver_only
def driver_report_details(request, report_id):
	report_pk = VehicleInspectionReport.objects.get(id=report_id)
	form = VehicleInspectionForm(request.POST or None, instance=report_pk)
	form.fields['repairStatus'].label = ""
	if form.is_valid():
		if "reopen-btn" in request.POST:
			post = form.save(commit=False)
			post.lastUpdatedUser = datetime.datetime.now()
			post._change_reason = 'Driver reopened ticket'
			post.repairStatus = False
			post.save()
			messages.success(request, ("Reopened Report!"))
			return redirect('report_list')
		else:
			post = form.save(commit=False)
			post.lastUpdatedUser = datetime.datetime.now()
			post._change_reason = 'Driver updated ticket'
			post.save()
			messages.success(request, ("Updated Report!"))
			return redirect('report_list')
	return render(request, 'driver_app/report_details.html', {
		'form':form, 'report_pk':report_pk
		})