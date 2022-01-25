from django.shortcuts import render, redirect
from django.contrib import messages
from driver_app.forms import VehicleInspectionForm
from driver_app.models import VehicleInspectionReport
from django.views.generic import ListView, DetailView
from django.urls import resolve
import datetime
from vehicle_website.wraps import mechanic_only
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator





@login_required
@mechanic_only
def mechanic_area(request):
	obj = VehicleInspectionReport.history.all()

	return render(request, 'mechanic_app/mechanic_area.html', {'object': obj})


@method_decorator(login_required, name='dispatch')
@method_decorator(mechanic_only, name='dispatch')
class mech_report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'mechanic_app/mech_report_list.html'
	ordering = ['-date']


@method_decorator(login_required, name='dispatch')
@method_decorator(mechanic_only, name='dispatch')
class completed_mech_report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'mechanic_app/completed_mech_report_list.html'
	ordering = ['-date']


@login_required
@mechanic_only
def mechanic_report_details(request, report_id):

	report_pk = VehicleInspectionReport.objects.get(id=report_id)
	form = VehicleInspectionForm(request.POST or None, instance=report_pk)
	form.fields['repairStatus'].label = ""
	if form.is_valid():
		if "complete-btn" in request.POST:
			post = form.save(commit=False)
			post.lastUpdatedMech = datetime.datetime.now()
			post._change_reason = 'Mechanic completed ticket'
			post.repairStatus = True
			post.save()
			messages.success(request, ("Completed Report!"))
			return redirect('mech_report_list')

		if "reopen-btn" in request.POST:
			post = form.save(commit=False)
			post.lastUpdatedMech = datetime.datetime.now()
			post.repairStatus = False
			post._change_reason = 'Mechanic reopened ticket'
			post.save()
			messages.success(request, ("Reopened Report!"))
			return redirect('mech_report_list')
		else:
			post = form.save(commit=False)
			post.lastUpdatedMech = datetime.datetime.now()
			post._change_reason = 'Mechanic updated ticket'
			post.save()
			messages.success(request, ("Saved Report!"))
			return redirect('mech_report_list')
			
	return render(request, 'mechanic_app/mech_report_details.html', {
		'form':form, 'report_pk':report_pk
		})