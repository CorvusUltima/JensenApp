"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpRequest, HttpResponseRedirect
from .models import Message, Room, Topic 
from .forms import RoomForm



def home(request):
    assert isinstance(request, HttpRequest)
    q=request.GET.get('q')  if request.GET.get('q') else ''
    topics=Topic.objects.all()
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)
    )
    room_count=rooms.count()
    context ={'rooms':rooms,'topics':topics, 'room_count':room_count,'title':'Home Page','year':datetime.now().year }
    return render(
        request,
        'MainPages/index.html',
      context
    )

def room (request,pk):
    room=Room.objects.get(id=pk)
    participants=room.participants.all()
    room_messages= room.message_set.all().order_by('-created')
    if request.method == "POST":
        message=Message.objects.create(
        owner=request.user,
        room=room,
        body=request.POST.get('body')
        )
        if room.participants.filter(id=request.user.id):  
            return redirect('room',pk) 
        else:
            room.participants.add(request.user)

        return redirect('room',pk)
    context={'room': room,'room_messages': room_messages,'participants':participants}
    return render (request, 'MainPages/room.html' , context )

def create_room(request):
    form = RoomForm()
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
    
            return redirect('account')
    context={'form':form}
    return render (request, 'MainPages/room-form.html' , context)



def update_room(request,pk):
    room = Room.objects.get(id=pk)
    print(room)
    form = RoomForm(instance = room )
    
    if request.method == 'POST':
        form=RoomForm(request.POST,instance = room)
        print('PRE-VALID')
      
        if form.is_valid():
            print('FORM IS VALID')
            form.save()
            return redirect('home')
    context={'form':form}
    return render (request, 'MainPages/room-form.html' , context)

def delete_message(request,pk):
    message=Message.objects.get(id=pk)
    print('PRE IF ')
    if request.user == message.owner:
        print('OWNERSHIP POSITIV')
        print('NOW DELETE')
        message.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def login_page(request):
    page = 'login'
    print(page)

    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':   
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            userAccount = authenticate(request,username=username,password=password)
            if userAccount is not None:
                login(request,userAccount)
                return redirect('home')
            else:
                messages.info(request,'Incorrect password entered. Please try again.')
        except:
            messages.info(request, 'Incorrect username or password entered. Please try again.')
    context={'page' : page}
    return render(request,'MainPages/login_registrate00.html',context)

def logout_page(request):
    logout(request)
    return redirect('home')
    
def register_page(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('profile-update' ,request.user.profile.id)
    else:
        form = UserCreationForm(request.POST)
    return render (request,'MainPages/login_registrate00.html',{'registration_form':form})

