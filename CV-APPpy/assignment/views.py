from django.shortcuts import render, redirect
from .models import Assignment, Applicant
from .forms import RegistrationForm

# Create your views here.


def form(request, assignment_slug):
    assignment= Assignment.objects.get(slug=assignment_slug)
    form=RegistrationForm(request.POST)
    if form.is_valid():
         user_email=form.cleaned_data['email']
         applicant,_ =Applicant.objects.get_or_create(email=user_email)

         applicant.email=user_email
         applicant.first_name=form.cleaned_data['first_name']
         applicant.last_name=form.cleaned_data['last_name']
         print(applicant.first_name)
         applicant.save()
         assignment.applicant.add(applicant)
         print('ovde sam ? ')
         print('name'+ applicant.first_name)
         return redirect('confirm-registration')
        
       

    context={'form':form}
    context_slug={'assignment': assignment}
    return render(request,'assignment/applicant-form.html', context,context_slug)


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