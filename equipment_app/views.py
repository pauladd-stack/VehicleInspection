from django.shortcuts import render, redirect


def equipment(request):
	return render(request, 'equipment_app/equipment.html', {})