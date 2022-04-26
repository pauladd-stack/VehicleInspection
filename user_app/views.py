from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout, update_session_auth_hash
from .models import User
from django.contrib import messages
from .forms import UserAdminCreationForm, UserAdminChangeForm, UserAdminChangeForm
from django.contrib.auth.forms import SetPasswordForm
from django.views.generic import ListView, DetailView
from driver_app.models import VehicleInspectionReport
import datetime
from vehicle_website.wraps import admin_only
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import csv
from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import letter 


@login_required
@admin_only
def register_user(request):
	if request.method== "POST":
		form = UserAdminCreationForm(request.POST)
		if form.is_valid():
			form.save()
			form.clean()
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = authenticate(email=email, password=password)
			messages.success(request, ("Created User!"))
			return redirect('user_list')
	else:
		form = UserAdminCreationForm()


@login_required
@admin_only
def update_user(request, user_id):
	
	user_pk = User.objects.get(id=user_id)

	if request.method == "POST":

		if 'user-submit' in request.POST:
			userform = UserAdminChangeForm(request.POST or None, instance=user_pk)
			pwform = SetPasswordForm(user=user_pk, data=request.POST)
			if userform.is_valid():
				userform.save()
				messages.success(request, ("Updated User!"))
				return redirect('user_list')
			else:
				messages.success(request, ("Error changing information!"))


		elif 'pw-submit' in request.POST:
			userform = UserAdminChangeForm(None, instance=user_pk)
			pwform = SetPasswordForm(user=user_pk, data=request.POST)
			if pwform.is_valid():
				pwform.save()
				update_session_auth_hash(request, pwform.user)
				messages.success(request, ("Updated User!"))
				return redirect('user_list')
			else:
				messages.success(request, ("Error changing information!"))


		else:
			messages.success(request, ("Something went wrong!"))
	else:
		userform = UserAdminChangeForm(request.POST or None, instance=user_pk)
		pwform = SetPasswordForm(user=user_pk, data=request.POST)


	return render(request, 'user_app/update_user.html', {
		'userform':userform, 'pwform':pwform, 'user_pk':user_pk
		})




@login_required
@admin_only
def delete_user(request, user_id):
	user = User.objects.get(id=user_id)
	user.delete()
	messages.success(request, ("Deleted User!"))
	return redirect('user_list')


@login_required
@admin_only
def change_password(request, user_id):
	user_pk = User.objects.get(id=user_id)
	form = SetPasswordForm(user=user_pk, data=request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, 'Your password was successfully updated!')
			return redirect('user_list')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = SetPasswordForm(user=user_pk)
	return render(request, 'user_app/change_password.html', {
		'form': form, 'user_pk':user_pk,
		})

@login_required
@admin_only
def delete_report(request, report_id):
	report = VehicleInspectionReport.objects.get(id=report_id)
	report._change_reason = 'Admin deleted report ' + str(VehicleInspectionReport.objects.get(id=report_id).equipment)
	report.lastUpdatedMech = datetime.datetime.now()
	report.delete()
	messages.success(request, ("Deleted Report!"))
	return redirect('mech_report_list')


@login_required
@admin_only
def report_pdf(request):
	buf = io.BytesIO()
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)

	
	reports = VehicleInspectionReport.objects.all()

	lines = []

	for report in reports:
		lines.append(f'{report.equipment}\n {report.driver}')

		

	for line in lines:
		textob.textLine(line)

	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	return FileResponse(buf, as_attachment=True, filename='report.pdf')


@login_required
@admin_only
def report_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=report.csv'

	writer = csv.writer(response)

	reports = VehicleInspectionReport.objects.all()

	writer.writerow(['Equipment', 'Driver', 'Date', 'Status'])

	for report in reports:
		writer.writerow([report.equipment, report.driver, report.date, report.repairStatus])

	return response


@method_decorator(login_required, name='dispatch')
@method_decorator(admin_only, name='dispatch')
class user_list(ListView):
	model = User
	template_name = "user_list.html"
	paginate_by = 20

	def get_queryset(self):
		email = self.request.GET.get('email')
		print(email)
		object_list = self.model.objects.all()
		if email:
			object_list = self.model.objects.filter(email__icontains=email)

		return object_list

	def get_context_data(self, **kwargs):
		context = super(user_list, self).get_context_data(**kwargs)
		context['form'] = UserAdminCreationForm()
		return context