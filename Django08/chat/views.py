from django.shortcuts import render, redirect
from .models import Rooms, Messages
from django.http import HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    rooms = Rooms.objects.all()
    return render(request, "chat/index.html", { "rooms" : rooms }) 

def chatroom(request, room_name):
    if request.user.is_authenticated is False:
        return redirect('/')
    room = Rooms.objects.get(name=room_name)
    messages = Messages.objects.filter(room=room.id).order_by("-submitted_at")[:3]
    return render(request, "chat/chatroom.html", { "room_name": room_name, "messages" : messages }) 
    
@require_POST
def message_save(request):
    try:
        text = request.POST.get('text')
        room = Rooms.objects.get(name=request.POST.get('room'))

        message = Messages(text=text, room=room, user=request.user)
        message.save()
        return HttpResponse(status=200)
    except ( Exception ) as e:
        return HttpResponse(str(e))
