from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'chat/index.html', {})

def Split(room_name):
    roomName = ''
    userName = ''

    idx = 0
    while room_name[idx] != '_':
        roomName += room_name[idx]
        idx += 1
    for i in range(idx+1, len(room_name)):
        userName+= room_name[i]
    
    return roomName,userName

def room(request, room_name):
    #room = lobby_Jinwoo
    #room[0] = lobby , room[1] = Jinwoo
    #user_name = room_name
    room_name, user_name = Split(room_name)
    #user_name = room_name
    return render(request,'chat/room.html',{
        'user_name_json': mark_safe(json.dumps(user_name)),
        'room_name_json': mark_safe(json.dumps(room_name))
    })