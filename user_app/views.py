from django.shortcuts import render

def home(request):
	return render(request, 'user_app/home.html', {})

def login(request):
	return render(request, 'user_app/login.html', {})