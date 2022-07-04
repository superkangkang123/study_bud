from django.shortcuts import render
from .models import Room

def home(request):
    rooms = Room.objects.all()
    return render(request,'base/home.html',{'rooms':rooms})

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'roomv':room}
    return render(request,'base/room.html',context)
