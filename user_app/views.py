from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages

def home(request):
	return render(request, 'user_app/home.html', {})

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