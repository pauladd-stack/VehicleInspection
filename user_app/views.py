from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from .forms import UserAdminCreationForm

def home(request):
	return render(request, 'user_app/home.html', {})


def admin_area(request):
	return render(request, 'user_app/admin.html', {})


def login_user(request):
	if request.method== "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		user =  authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, ("There was an error while logging you in!"))
			return redirect('login')


	else:
		return render(request, 'user_app/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("Logged Out!"))
	return redirect('home')

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
	
	