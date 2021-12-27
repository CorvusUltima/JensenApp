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
        profile = Profile.objects.get(id=pk)
        assignments = [_ for _ in Assignment.objects.filter(host=request.user)]
        
        
        context={'assignments':assignments,'profile':profile}
    
        return render(request,'ProfilePages/profile-page.html',context)
    return redirect('login')


def profile_update(request, pk):
    if(request.user.is_authenticated | request.user.is_superuser):
        profile = Profile.objects.get(id=pk)
        form = CreateProfileForm(instance=profile)
        if request.method=='POST':
            form=CreateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form': form}
        return render(request,'ProfilePages/profile-update.html',context)
    else:
        return redirect('home')


def account(request):
    id = request.user.profile.id
    profile = Profile.objects.get(id = id)
    assignments = [_ for _ in Assignment.objects.filter(host=request.user)]
    context = {'assignments':assignments, 'profile' : profile}
    return render(request,'ProfilePages/account.html',context)
