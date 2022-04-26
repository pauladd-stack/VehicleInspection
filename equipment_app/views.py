from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
import datetime
from vehicle_website.wraps import mechanic_only
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from equipment_app.models import Equipment
from driver_app.models import VehicleInspectionReport
from .forms import DriverChangeForm

from .utils import get_plot

@method_decorator(login_required, name='dispatch')
@method_decorator(mechanic_only, name='dispatch')
class equipment_list(ListView):
	model = Equipment
	template_name = 'equipment_app/equipment_list.html'
	ordering = ['id']
	paginate_by = 50

	def get_queryset(self):
		equipment = self.request.GET.get('equipment')
		print(equipment)
		object_list = self.model.objects.all()
		if equipment:
			object_list = self.model.objects.filter(equipment__icontains=equipment)

		return object_list


@login_required
@mechanic_only
def equipment_details(request, equip_id):
	equip_pk = Equipment.objects.get(id=equip_id)
	vir_pk = VehicleInspectionReport.objects.filter(equipment=equip_id)
	engcount = 0
	transcount = 0
	reportcount = 0

	for vir in vir_pk:
		if equip_pk == vir.equipment:
			reportcount += 1
			if vir.engine_check == True:
				engcount += 1
			elif vir.transmission_check == True:
				transcount += 1
			
	y = [engcount, transcount]
	x = ['engine', 'transmission']
	chart = get_plot(x,y)

	if request.method == "POST":
		driverForm = DriverChangeForm(request.POST or None, instance=equip_pk)
		if driverForm.is_valid():
			driver = form.save(commit=False)
			driver.save()
			messages.success(request, 'Submitted')
			return redirect('inspection_report')
			
	else:
		driverForm = DriverChangeForm(request.POST or None, instance=equip_pk)

	


	
	return render(request, 'equipment_app/equipment_details.html', {
		'equip_pk':equip_pk, 'vir_pk':vir_pk, 'form': driverForm, 'chart': chart, 'reportcount': reportcount
		})