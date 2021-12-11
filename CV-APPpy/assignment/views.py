from django.shortcuts import render, redirect
from .models import Assignment, Applicant, Location
from .forms import RegistrationForm ,AssignmentForm

# Create your views here.


def apply(request, assignment_slug):

    assignment=Assignment.objects.get(slug=assignment_slug)
    form = RegistrationForm(request.POST)

    if form.is_valid():
        applicant,_ = Applicant.objects.get_or_create(**form.cleaned_data)
        assignment.applicant.add(applicant)
        return redirect('confirm-registration')
     
       
    context={'form':form,'assignment' : assignment}
    return render(request,'assignment/applicant-form.html',context)


def index(request):
   
    assignments = Assignment.objects.all()

    return render(request, 'assignment/index.html',
                  {'isActive': True, 'assignments': assignments})


def get_all_user_assignments(request):
    assignments = []
    for assignment in Assignment.objects.filter(host=request.user):
        assignments.append(assignment)
    context={'assignments':assignments}
    return render(request,'profile',context)



def create_assignment(request):
    form = AssignmentForm()
    if request.method=='POST':
        form=AssignmentForm(request.POST)
        if form.is_valid():
           assignment=form.save(commit= False)
           assignment.host=request.user
           assignment.slug=assignment.title.lower().replace(' ', '-')
           assignment.save()
           
        return redirect('profile')
    context={'form':form}
    return render(request,'assignment/create-assignment.html',context)





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


