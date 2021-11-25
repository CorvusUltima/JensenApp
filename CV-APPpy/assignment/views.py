from django.shortcuts import render, redirect
from .models import Assignment, Applicant
from .forms import RegistrationForm

# Create your views here.
def home(request):
    return(request,'assignment/home.html')


def index(request):
   
    assignments = Assignment.objects.all()

    return render(request, 'assignment/index.html',
                  {'isActive': True, 'assignments': assignments})


def assignment_details(request, assignment_slug):
    try: 
          assignment= Assignment.objects.get(slug=assignment_slug)
          if  request.method == 'GET':
               registration_form = RegistrationForm()
            
          else:
               registration_form = RegistrationForm(request.POST)
               if registration_form.is_valid():
                   user_email= registration_form.cleaned_data['email']
                   applicant, _ =Applicant.objects.get_or_create(email=user_email)
                   assignment.applicant.add(applicant)
                   return redirect('confirm-registration')

          return render(request, 'assignment/assignment-details.html',
                         {    'assignment_found': True,
                              'assignment': assignment ,
                              'form':  registration_form
                          })
                                       
    except Exception as exc:
         print(exc)
         return render(request, 'assignment/assignment-details.html',
                  { 'assignment_found': False
                   })

def registration_confirmation(request):
    return render(request, 'assignment/registration-success.html')