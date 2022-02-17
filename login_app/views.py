from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout, update_session_auth_hash
from user_app.models import User
from django.contrib import messages
from user_app.forms import ProfileUserChangeForm, ProfilePasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm
import datetime
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

'''
def login_user(request):
	if request.method== "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		user =  authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			if request.user.role == 'Driver':
				return redirect('driver_area')
			elif request.user.role == 'Mechanic':
				return redirect('mechanic_area')
			elif request.user.role == 'Admin':
				return redirect('admin_area')
			else:
				return redirect('home')
		else:
			messages.error(request, ("There was an error while logging you in!"))
			return redirect('login')


	else:
		return render(request, 'login_app/login.html', {})
'''

def login_user(request):
	if request.method== "POST":
		form = LoginForm(request.POST)
		email = request.POST['email']
		password = request.POST['password']
		user =  authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			if request.user.role == 'Driver':
				return redirect('driver_area')
			elif request.user.role == 'Mechanic':
				return redirect('mechanic_area')
			elif request.user.role == 'Admin':
				return redirect('admin_area')
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
