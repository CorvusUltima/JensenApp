from django.http import request
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required



# Create your views here.

def profile_page(request):
    if request.user.is_authenticated:
        return render(request,'user_profile/profile-page.html')
    
    return redirect('login')

