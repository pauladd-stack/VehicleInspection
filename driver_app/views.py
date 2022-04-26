from django.shortcuts import render, redirect
from .forms import VehicleInspectionForm, ReadVehicleInspectionForm, MechVehicleInspectionForm
from .models import VehicleInspectionReport
from django.contrib import messages
from django.views.generic import ListView, DetailView
import datetime
from vehicle_website.wraps import driver_only
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from equipment_app.models import Equipment
from notification_app.forms import NotificationForm
from django.db.models import Q



from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()


@login_required
@driver_only
def inspection_report(request):
	if request.method == "POST":
		form = VehicleInspectionForm(request.POST)
		if form.is_valid():
			driver = form.save(commit=False)
			driver.driver = request.user
			driver.repairStatus = False
			equip = Equipment.objects.get(id = request.POST['equipment'])
			driver.equipment = equip
			driver.lastUpdatedUser = datetime.datetime.now()
			driver._change_reason = str(request.user) + ' created a new ticket'
			driver.save()
			messages.success(request, 'Submitted')
			return redirect('report_list')
		else:
			messages.error(request, 'Please correct the error below.')
			
	else:
		form = VehicleInspectionForm()
	equipment = Equipment.objects.all()
	

@method_decorator(login_required, name='dispatch')
@method_decorator(driver_only, name='dispatch')
class report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'driver_app/report_list.html'

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

	def get_context_data(self, **kwargs):
		context = super(report_list, self).get_context_data(**kwargs)
		context['form'] = VehicleInspectionForm()
		context['equipment_list'] = equipment = Equipment.objects.all()
		return context


@method_decorator(login_required, name='dispatch')
@method_decorator(driver_only, name='dispatch')
class completed_driver_report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'driver_app/completed_driver_report_list.html'
	ordering = ['date']
	paginate_by = 50

	def get_queryset(self):
		equipment = self.request.GET.get('equipment')
		print(equipment)
		object_list = self.model.objects.all()
		if equipment:
			object_list = self.model.objects.filter(Q(equipment__equipment_type__icontains=equipment) | Q(equipment__equipment__icontains=equipment))

		return object_list


@login_required
@driver_only
def driver_report_details(request, report_id):
	report_pk = VehicleInspectionReport.objects.get(id=report_id)
	print(report_pk.repairStatus)
	form = VehicleInspectionForm(request.POST or None, instance=report_pk)
	if form.is_valid():
		if "updated-btn" in request.POST:
			post = form.save(commit=False)
			post.lastUpdatedUser = datetime.datetime.now()
			post._change_reason = str(request.user) + ' updated ticket'
			post.save()
			messages.success(request, ("Updated Report!"))
			return redirect('report_list')
			
	return render(request, 'driver_app/report_details.html', {
		'form':form, 'report_pk':report_pk
		})

@login_required
@driver_only
def completed_driver_report_details(request, report_id):
	report_pk = VehicleInspectionReport.objects.get(id=report_id)
	print(report_pk.repairStatus)
	form = ReadVehicleInspectionForm(request.POST or None, instance=report_pk)
	if form.is_valid():
		if "reopen-btn" in request.POST:
			post = form.save(commit=False)
			post.lastUpdatedUser = datetime.datetime.now()
			post._change_reason = str(request.user) + ' reopened ticket'
			post.repairStatus = False
			post.save()
			messages.success(request, ("Reopened Report!"))
			return redirect('report_list')

	return render(request, 'driver_app/completed_driver_report_details.html', {
		'form':form, 'report_pk':report_pk
		})