from django import forms
from django.http import request
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from assignment.models import Assignment
from ProfilePages.forms import CreateProfileForm
from ProfilePages.models import Profile



# Create your views here.
def profiles(request):
     return render(request,'ProfilePages/profiles.html')

def profile_page(request,pk):
    if request.user.is_authenticated:
        assignments = []
        profile = Profile.objects.get(id=pk)
        for assignment in Assignment.objects.filter(host=request.user):
            assignments.append(assignment)
        context={'assignments':assignments,'profile':profile}
    
        return render(request,'ProfilePages/profile-page.html',context)
    

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
    return render(request,'ProfilePages/profile-update.html',context)

def test(request):
    ob=353
    context={'ob':ob}

    return render(request,'ProfilePages/test.html',context)
