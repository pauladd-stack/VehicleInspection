from django.shortcuts import render, redirect
from .forms import VehicleInspectionForm
from .models import VehicleInspectionReport
from django.contrib import messages
from django.views.generic import ListView, DetailView
import datetime
from vehicle_website.wraps import driver_only
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from equipment_app.models import Equipment

@login_required
@driver_only
def driver_area(request):
	dates = []
	obj = VehicleInspectionReport.history.all()

	current_user = request.user
	orderby = VehicleInspectionReport.objects.order_by('-date')
	for order in orderby:
		if current_user == order.driver:
			dates.append(order.date)

	if not dates:
		dates.append(0)

	latest_report = dates[0]
	#last_week = datetime.date.today() - date.timedelta(days=7)
	today = datetime.date.today()
	start = today - datetime.timedelta(days=today.weekday())
	end = start + datetime.timedelta(days=6)

	return render(request, 'driver_app/driver_area.html', {'object': obj, 'latest':latest_report, 'start':start, 'end':end})

@login_required
@driver_only
def inspection_report(request):
	if request.method == "POST":
		form = VehicleInspectionForm(request.POST)
		if form.is_valid():
			driver = form.save(commit=False)
			driver.driver = request.user
			driver.repairStatus = False
			driver.equipment = request.POST['equipment']
			driver.lastUpdatedUser = datetime.datetime.now()
			driver._change_reason = str(request.user) + ' created a new ticket'
			driver.save()
			messages.success(request, 'Submitted')
			return redirect('inspection_report')
		else:
			messages.error(request, 'Please correct the error below.')
			
	else:
		form = VehicleInspectionForm()
		
	equipment = Equipment.objects.all()
	return render(request, 'driver_app/inspection_report.html', {
		'form': form, 'equipment': equipment,
		})


@method_decorator(login_required, name='dispatch')
@method_decorator(driver_only, name='dispatch')
class report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'driver_app/report_list.html'
	ordering = ['-date']

	def get_queryset(self):
		equipment = self.request.GET.get('equipment')
		object_list = self.model.objects.all()
		if equipment:
			object_list = self.model.objects.filter(equipment__icontains=equipment)

		return object_list


@method_decorator(login_required, name='dispatch')
@method_decorator(driver_only, name='dispatch')
class completed_driver_report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'driver_app/completed_driver_report_list.html'
	ordering = ['-date']

	def get_queryset(self):
		equipment = self.request.GET.get('equipment')
		print(equipment)
		object_list = self.model.objects.all()
		if equipment:
			object_list = self.model.objects.filter(equipment__icontains=equipment)

		return object_list


@login_required
@driver_only
def driver_report_details(request, report_id):
	report_pk = VehicleInspectionReport.objects.get(id=report_id)
	form = VehicleInspectionForm(request.POST or None, instance=report_pk)
	if form.is_valid():
		if "reopen-btn" in request.POST:
			post = form.save(commit=False)
			post.lastUpdatedUser = datetime.datetime.now()
			post._change_reason = str(request.user) + ' reopened ticket'
			post.repairStatus = False
			post.save()
			messages.success(request, ("Reopened Report!"))
			return redirect('report_list')
		else:
			post = form.save(commit=False)
			post.lastUpdatedUser = datetime.datetime.now()
			post._change_reason = str(request.user) + ' updated ticket'
			post.save()
			messages.success(request, ("Updated Report!"))
			return redirect('report_list')
	return render(request, 'driver_app/report_details.html', {
		'form':form, 'report_pk':report_pk
		})