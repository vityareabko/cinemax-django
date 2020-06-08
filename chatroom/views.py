from django.shortcuts import render



def index(request):
    return render(request, 'chatroom/chatroom.html')

def room(request, room_name):
    return render(request, 'chatroom/room.html', {
        'room_name': room_name
    })