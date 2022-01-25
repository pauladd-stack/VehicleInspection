from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout, update_session_auth_hash
from .models import User
from django.contrib import messages
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import ListView, DetailView
from driver_app.models import VehicleInspectionReport
import datetime
from vehicle_website.wraps import admin_only
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
			return redirect('register_user')
	else:
		form = UserAdminCreationForm()
	return render(request, 'user_app/register_user.html', {
		'form':form
		})


@login_required
@admin_only
def update_user(request, user_id):
	user_pk = User.objects.get(id=user_id)
	form = UserAdminChangeForm(request.POST or None, instance=user_pk)
	if form.is_valid():
		form.save()
		messages.success(request, ("Updated User!"))
		return redirect('user_list')
	return render(request, 'user_app/update_user.html', {
		'form':form, 'user_pk':user_pk
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
	form = PasswordChangeForm(user=user_pk, data=request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, 'Your password was successfully updated!')
			return redirect('user_list')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(user=user_pk)
	return render(request, 'user_app/change_password.html', {
		'form': form, 'user_pk':user_pk,
		})

@login_required
@admin_only
def admin_area(request):
	obj = VehicleInspectionReport.history.all()

	return render(request, 'user_app/admin_area.html', {'object': obj})



@login_required
@admin_only
def delete_report(request, report_id):
	report = VehicleInspectionReport.objects.get(id=report_id)
	report._change_reason = 'Admin deleted report ' + VehicleInspectionReport.objects.get(id=report_id).truck
	report.lastUpdatedMech = datetime.datetime.now()
	report.delete()
	messages.success(request, ("Deleted Report!"))
	return redirect('mech_report_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(admin_only, name='dispatch')
class user_list(ListView):
	model = User
	template_name = "user_list.html"
