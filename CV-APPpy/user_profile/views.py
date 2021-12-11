from django.http import request
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from assignment.models import Assignment



# Create your views here.

def profile_page(request):
    if request.user.is_authenticated:
        assignments = []
        for assignment in Assignment.objects.filter(host=request.user):
            assignments.append(assignment)
        context={'assignments':assignments}
    
        return render(request,'user_profile/profile-page.html',context)
    
    return redirect('login')

