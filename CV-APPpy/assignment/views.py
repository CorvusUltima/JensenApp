from django.shortcuts import render, redirect
from .models import Assignment, Applicant
from .forms import RegistrationForm

# Create your views here.


def apply(request, assignment_slug):

    assignment=Assignment.objects.get(slug=assignment_slug)
    form = RegistrationForm(request.POST)

    if form.is_valid():
        print('usli smo u if  ')
        user_email = form.cleaned_data['email']
        applicant, _ = Applicant.objects.get_or_create(email=user_email)
        applicant.first_name=form.cleaned_data['first_name']
        assignment.applicant.add(applicant)
        return redirect('confirm-registration')
     
       
    context={'form':form,'assignment' : assignment}
    return render(request,'assignment/applicant-form.html',context)


def index(request):
   
    assignments = Assignment.objects.all()

    return render(request, 'assignment/index.html',
                  {'isActive': True, 'assignments': assignments})


def assignment_details(request, assignment_slug):
    try: 
          assignment= Assignment.objects.get(slug=assignment_slug)
          return render(request, 'assignment/assignment-details.html',
                         {    'assignment_found': True,
                              'assignment': assignment 
                          })
                                       
    except Exception as exc:
         print(exc)
         return render(request, 'assignment/assignment-details.html',
                  { 'assignment_found': False
                   })

def registration_confirmation(request):
    return render(request, 'assignment/registration-success.html')

def user_home_page(request):
    return render(request,'assignment/profile.html')

def create_assignment(request):
    context={}
    return render(request,create-assignment.html,context)