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
    page = 'login'
    print(page)

    if request.user.is_authenticated:
        return redirect('home')
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


    context={'page' : page}
    print(context)
    return render(request,'app/login_registrate00.html',context)

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
            redirect('home')
        else :
            messages.error(request,'message')

    return render (request,'app/login_registrate00.html',{'form':form})
    
    
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
