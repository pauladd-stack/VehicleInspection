from django.shortcuts import render, redirect

def home(request):
	return render(request, 'general_app/home.html', {})
