from django.http.response import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from assignment.models import Applicant, Assignment
from ProfilePages.forms import CreateProfileForm
from ProfilePages.models import Profile



# Create your views here.
def profiles(request):
     return render(request,'ProfilePages/profiles.html')

def profile_page(request,pk):

    profile = Profile.objects.get(id=pk)
    assignments = [_ for _ in Assignment.objects.filter(host=request.user)]
    
    
    context={'assignments':assignments,'profile':profile}

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
    assignments = [_ for _ in Assignment.objects.filter(host=request.user)]
    context = {'assignments':assignments, 'profile' : profile}
    return render(request,'ProfilePages/account.html',context)

def cancel_assignment(request,pk):

    try:
        assignment = request.user.profile.assignments.get(id=pk)
    except  Assignment.DoesNotExist:
        assignment = None
        
    #applicant = Applicant.objects.filter(owner=request.user).first()
    a_list = [a for a in assignment.applicant.all() if a.owner == request.user]
    if assignment:
        assignment.applicant.remove(*a_list)
        a_list[0].delete()
        request.user.profile.assignments.remove(assignment)
        
          
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    
