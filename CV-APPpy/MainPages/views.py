"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.urls import reverse

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
        pasword=request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            userAccount = authenticate(request,username=username,password=pasword)
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
    form= UserCreationForm()

    if request.method=='POST':
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            named_redirect = reverse('profile', args=[str(request.user.profile.id)])
            return redirect(named_redirect)
        else :
            messages.error(request,'message')
    return render (request,'MainPages/login_registrate00.html',{'form':form})
    
    
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
