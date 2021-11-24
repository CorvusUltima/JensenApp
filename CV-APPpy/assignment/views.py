from django.shortcuts import render
from .models import Assignment
from .forms import RegistrationForm

# Create your views here.

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
                   applicant = registration_form.save()
                   assignment.applicant.add(applicant)

          return render(request, 'assignment/assignment-details.html',
                         {    'assignment_found': True,
                              'assignment': assignment ,
                              'form': registration_form
                          })
                                       
    except Exception as exc:
         return renderd(request, 'assignment/assignment-details.html',
                  { 'assignment_found': False,
                   
                   })
