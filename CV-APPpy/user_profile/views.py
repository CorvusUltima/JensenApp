from django import forms
from django.http import request
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from assignment.models import Assignment
from user_profile.forms import CreateProfileForm
from user_profile.models import Profile



# Create your views here.
def profiles(request):
     return render(request,'user_profile/profiles.html')

def profile_page(request):
    if request.user.is_authenticated:
        assignments = []
        profile = Profile.objects.get(user=request.user)
        for assignment in Assignment.objects.filter(host=request.user):
            assignments.append(assignment)
        context={'assignments':assignments,'profile':profile}
    
        return render(request,'user_profile/profile-page.html',context)
    

    return redirect('login')


def profile_update(request):


    profile=Profile.objects.get(user=request.user)
    form=CreateProfileForm(instance=profile)
    if request.method=='POST':
        form=CreateProfileForm(request.POST,instance=profile)
        if form.is_valid():
           form.save()
        return redirect('profile')
           
    context={'form': form}
    return render(request,'user_profile/profile-update.html',context)

def test(request):
    ob=353
    context={'ob':ob}

    return render(request,'user_profile/test.html',context)

