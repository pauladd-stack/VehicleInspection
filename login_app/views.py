from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout, update_session_auth_hash
from user_app.models import User
from django.contrib import messages
from user_app.forms import ProfileUserChangeForm, ProfilePasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm
import datetime
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

from driver_app.models import VehicleInspectionReport



@login_required
def dashboard(request):
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

	return render(request, 'login_app/dashboard.html', {'object': obj, 'latest':latest_report, 'start':start, 'end':end})




def login_user(request):
	if request.method== "POST":
		form = LoginForm(request.POST)
		email = request.POST['email']
		password = request.POST['password']
		user =  authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			if request.user.role == 'Driver':
				return redirect('dashboard')
			elif request.user.role == 'Mechanic':
				return redirect('dashboard')
			elif request.user.role == 'Admin':
				return redirect('dashboard')
			else:
				return redirect('home')
		else:
			messages.success(request, ("Your username or password is incorrect!"))
			return redirect('login')


	else:
		form = LoginForm()
	return render(request, 'login_app/login.html', {'form': form,})



@login_required
def logout_user(request):
	logout(request)
	messages.success(request, ("Logged Out!"))
	return redirect('home')





@login_required
def user_profile(request, user_id):
	
	user_pk = User.objects.get(id=user_id)

	if request.method == "POST":

		if 'user-submit' in request.POST:
			userform = ProfileUserChangeForm(request.POST or None, instance=user_pk)
			pwform = ProfilePasswordChangeForm(None, instance=user_pk)
			if userform.is_valid():
				userform.save()
				messages.success(request, ("Updated User!"))
			else:
				messages.success(request, ("Error changing information!"))


		elif 'pw-submit' in request.POST:
			userform = ProfileUserChangeForm(None, instance=user_pk)
			pwform = ProfilePasswordChangeForm(request.POST or None, instance=user_pk)
			if pwform.is_valid():
				pwform.save()
				update_session_auth_hash(request, pwform.user)
				messages.success(request, ("Updated User!"))
			else:
				messages.success(request, ("Error changing information!"))


		else:
			messages.success(request, ("Something went wrong!"))
	else:
		userform = ProfileUserChangeForm(request.POST or None, instance=user_pk)
		pwform = ProfilePasswordChangeForm(request.POST or None, instance=user_pk)


	return render(request, 'login_app/user_profile.html', {
		'userform':userform, 'pwform':pwform, 'user_pk':user_pk
		})
