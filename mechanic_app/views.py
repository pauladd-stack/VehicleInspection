from django.shortcuts import render, redirect
from django.contrib import messages
from driver_app.forms import VehicleInspectionForm, MechVehicleInspectionForm, ReadVehicleInspectionForm
from driver_app.models import VehicleInspectionReport
from django.views.generic import ListView, DetailView
from django.urls import resolve
import datetime
from vehicle_website.wraps import mechanic_only
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q




@method_decorator(login_required, name='dispatch')
@method_decorator(mechanic_only, name='dispatch')
class mech_report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'mechanic_app/mech_report_list.html'


	def get_queryset(self):
		equipment = self.request.GET.get('equipment')
		ordering = self.request.GET.get('ordering')
		report_list = self.request.GET.get('reportlist-radio1')
		print(report_list)
		object_list = self.model.objects.all()

		if equipment:
			object_list = self.model.objects.filter(Q(equipment__equipment_type__icontains=equipment) | Q(equipment__equipment__icontains=equipment))
		elif ordering:
			if ordering == "Date":
				object_list = self.model.objects.all().order_by('-date')
			elif ordering == "Driver":
				object_list = self.model.objects.all().order_by('-driver')
			elif ordering == "Report":
				object_list = self.model.objects.all().order_by('-equipment')

		else:
			object_list = self.model.objects.all().order_by('-date')

		return object_list




@method_decorator(login_required, name='dispatch')
@method_decorator(mechanic_only, name='dispatch')
class completed_mech_report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'mechanic_app/completed_mech_report_list.html'
	ordering = ['date']
	

	def get_queryset(self):
		equipment = self.request.GET.get('equipment')
		object_list = self.model.objects.all()
		if equipment:
			object_list = self.model.objects.filter(Q(equipment__equipment_type__icontains=equipment) | Q(equipment__equipment__icontains=equipment))

		return object_list


@login_required
@mechanic_only
def mechanic_report_details(request, report_id):

	report_pk = VehicleInspectionReport.objects.get(id=report_id)
	form = MechVehicleInspectionForm(request.POST or None, instance=report_pk)
	if request.method == "POST":
		if form.is_valid():
			if "complete-btn" in request.POST:
				post = form.save(commit=False)
				post.lastUpdatedMech = datetime.datetime.now()
				post.assignedMech = str(request.user);
				post._change_reason = str(request.user) + ' completed ticket'
				post.repairStatus = True
				post.save()
				messages.success(request, ("Completed Report!"))
				return redirect('mech_report_list')

			else:
				post = form.save(commit=False)
				post.lastUpdatedMech = datetime.datetime.now()
				post._change_reason = str(request.user) + ' updated ticket'
				post.save()
				messages.success(request, ("Saved Report!"))
				return redirect('mech_report_list')
		else:
			messages.success(request, ("ERROR!"))


			
	return render(request, 'mechanic_app/mech_report_details.html', {
		'form':form, 'report_pk':report_pk
		})

@login_required
@mechanic_only
def completed_mechanic_report_details(request, report_id):

	report_pk = VehicleInspectionReport.objects.get(id=report_id)
	form = ReadVehicleInspectionForm(request.POST or None, instance=report_pk)
	if request.method == "POST":
		if form.is_valid():
			if "reopen-btn" in request.POST:
				post = form.save(commit=False)
				post.lastUpdatedMech = datetime.datetime.now()
				post.repairStatus = False
				post._change_reason = str(request.user) + ' reopened ticket'
				post.save()
				messages.success(request, ("Reopened Report!"))
				return redirect('completed_mech_report_list')

		else:
			messages.success(request, ("ERROR!"))


			
	return render(request, 'mechanic_app/completed_mech_report_details.html', {
		'form':form, 'report_pk':report_pk
		})