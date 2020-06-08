from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request):
    return render(request, 'chatroom/chatroom.html')

@login_required
def room(request, room_name):
    return render(request, 'chatroom/room.html', {
        'room_name_json': room_name, #room_name
        'username': request.user.username, #request.user.username
    })