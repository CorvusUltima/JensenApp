
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from ProfilePages.forms import CreateProfileForm
from ProfilePages.models import Profile



# Create your views here.
def profiles(request):
     return render(request,'ProfilePages/profiles.html')

def profile_page(request,pk):

    profile = Profile.objects.get(id=pk)  
    context={'profile':profile}

    return render(request,'ProfilePages/profile-page.html',context)

@login_required(login_url = 'login')
def profile_update(request, pk):
   
        profile = Profile.objects.get(id=pk)
        form = CreateProfileForm(instance=profile)
        if request.method=='POST':
            form=CreateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                profile=form.save(commit= False)
                profile.save()
                return redirect('account')
        context = {'form': form}
        return render(request,'ProfilePages/profile-update.html',context)
    

@login_required(login_url = 'login')
def account(request):
    id = request.user.profile.id
    profile = Profile.objects.get(id = id)
    print(profile)
    #assignments = [_ for _ in Assignment.objects.filter(host=request.user)]
    
    context = { 'profile' : profile}
    return render(request,'ProfilePages/account.html',context)



    
