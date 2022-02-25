from django.shortcuts import render, redirect
from django.contrib import messages
from driver_app.forms import VehicleInspectionForm, MechVehicleInspectionForm
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

	return render(request, 'mechanic_app/mechanic_area.html', {'object': obj, 'latest':latest_report, 'start':start, 'end':end})


@method_decorator(login_required, name='dispatch')
@method_decorator(mechanic_only, name='dispatch')
class mech_report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'mechanic_app/mech_report_list.html'
	ordering = ['-date']

	def get_queryset(self):
		equipment = self.request.GET.get('equipment')
		object_list = self.model.objects.all()
		if equipment:
			object_list = self.model.objects.filter(equipment__icontains=equipment)

		return object_list

@method_decorator(login_required, name='dispatch')
@method_decorator(mechanic_only, name='dispatch')
class completed_mech_report_list(ListView):
	model = VehicleInspectionReport
	template_name = 'mechanic_app/completed_mech_report_list.html'
	ordering = ['-date']

	def get_queryset(self):
		equipment = self.request.GET.get('equipment')
		object_list = self.model.objects.all()
		if equipment:
			object_list = self.model.objects.filter(equipment__icontains=equipment)

		return object_list


@login_required
@mechanic_only
def mechanic_report_details(request, report_id):

	report_pk = VehicleInspectionReport.objects.get(id=report_id)
	form = MechVehicleInspectionForm(request.POST or None, instance=report_pk)
	if form.is_valid():
		if "complete-btn" in request.POST:
			post = form.save(commit=False)
			post.lastUpdatedMech = datetime.datetime.now()
			post._change_reason = str(request.user) + ' completed ticket'
			post.repairStatus = True
			post.save()
			messages.success(request, ("Completed Report!"))
			return redirect('mech_report_list')

		if "reopen-btn" in request.POST:
			post = form.save(commit=False)
			post.lastUpdatedMech = datetime.datetime.now()
			post.repairStatus = False
			post._change_reason = str(request.user) + ' reopened ticket'
			post.save()
			messages.success(request, ("Reopened Report!"))
			return redirect('mech_report_list')
		else:
			post = form.save(commit=False)
			post.lastUpdatedMech = datetime.datetime.now()
			post._change_reason = str(request.user) + ' updated ticket'
			post.save()
			messages.success(request, ("Saved Report!"))
			return redirect('mech_report_list')
			
	return render(request, 'mechanic_app/mech_report_details.html', {
		'form':form, 'report_pk':report_pk
		})