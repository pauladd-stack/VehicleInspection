from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required
def chat(request):

	return render(request, 'chat_app/chat.html', {})

@login_required
def room(request, room_name):
    return render(request, 'chat_app/room.html', {'room_name': room_name})
