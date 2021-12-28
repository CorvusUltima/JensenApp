"""
Definition of views.
"""

from datetime import datetime
from typing import ContextManager
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.urls import reverse
from MainPages.forms import RegistrationForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'MainPages/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

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
            # Alternatively
            # user = form.cleaned_data.get('username')
            # user = user.lower()
            # raw_password = form.cleaned_data.get('password')
            # authenticate(username=user, password=raw_password)
            login(request,user)
            return redirect('profile-update' ,request.user.profile.id)
    else:
        form = UserCreationForm()
    return render (request,'MainPages/login_registrate00.html',{'registration_form':form})


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'MainPages/contact.html',
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
        'MainPages/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
