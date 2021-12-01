"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def login_page(request):
    if request.method=='POST':   
        username=request.POST.get('username')
        pasword=request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'user does not exists ')
        
        user= authenticate(request,username=username,password=pasword)
       

        if user is not None:
            login(request,user)
            return redirect('home')
        else :
             messages.error(request,'username or password does not exist ')


    context={}
    return render(request,'app/login_registrate00.html')


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
