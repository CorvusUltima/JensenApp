
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from ProfilePages.forms import CreateProfileForm
from ProfilePages.models import Profile
from MainPages.models import Message , Topic ,Room




# Create your views here.
def profiles(request):
     return render(request,'ProfilePages/profiles.html')
@login_required(login_url = 'login')
def profile_page(request,pk):
    topics=Topic.objects.all()
    rooms=Room.objects.filter(host=request.user)
    room_messages=Message.objects.filter()
    profile = Profile.objects.get(id=pk)  
    context={'profile':profile,'room_messages':room_messages,'topics':topics,'rooms':rooms}

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
    room_messages=Message.objects.filter()  
    context = { 'profile' : profile ,'room_messages' : room_messages}
    return render(request,'ProfilePages/account.html',context)



    
