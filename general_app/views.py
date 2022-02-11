from django.shortcuts import render, redirect



def home(request):
	return render(request, 'general_app/home.html', {})

def pricing(request):
	return render(request, 'general_app/pricing.html', {})

def features(request):
	return render(request, 'general_app/features.html', {})


def handler404(request, *args, **argv):
	return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
	return render(request, '500.html', status=500)

def handler403(request, *args, **argv):
	return render(request, '403.html', status=403)

def handler400(request, *args, **argv):
	return render(request, '400.html', status=400)
