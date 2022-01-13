from django.shortcuts import render, redirect
from .models import Assignment, Applicant, Location, Tag, models
from .forms import AssignmentForm, TagForm

# Create your views here.


def apply(request, pk):

    assignment=Assignment.objects.get(id=pk)
    applicant=Applicant(owner=request.user)
    applicant.save()
   
    if  applicant not in assignment.applicant.all():
        assignment.applicant.add(applicant)
        assignment.save()
        request.user.profile.assignments.add(assignment)
        return redirect('assignment-details',pk)
    return redirect('all-assignments')



def index(request):
    text = request.GET.get('text')
    print(str(text))
    if(text is None):
        assignments = Assignment.objects.all()
    else:
        assignments = Assignment.objects.filter(
            models.Q(title__icontains = text) |
            models.Q(host__username__icontains = text) |
            models.Q(description__icontains = text)
            )

    return render(request, 'Assignment/assignments-all.html',
                  {'isActive': True, 'assignments': assignments})


def create_assignment(request):
    tags = Tag.objects.all()
    form = AssignmentForm()

    tag_form = TagForm()
    form.initial['Title'] = "TEST"
    if request.method=='POST':
        form=AssignmentForm(request.POST,request.FILES )
        tag_form = TagForm(request.POST)
        
        if 'add_tag' in request.POST:
            print('Add tag')
            if tag_form.is_valid:
                tag_form.save()
        if 'Submit' in request.POST: 
             if form.is_valid:
                    assignment= form.save(commit=False)
                    assignment.host=request.user
                    assignment.save()
                    return redirect('account')
                 
    
    context={'form':form ,'tag_form':tag_form ,'tags' : tags}
    return render(request,'Assignment/assignment-form.html',context)


def update_assignment(request,pk):
    
    assignment =Assignment.objects.get(id=pk)
    form = AssignmentForm(instance= assignment)
    if request.method=='POST':
        form=AssignmentForm(request.POST,request.FILES,instance=assignment)
        if form.is_valid():
            assignment=form.save(commit= False)
            assignment.host=request.user
            assignment.save()
            return redirect('account')
    context={'form':form}
    return render(request,'Assignment/assignment-form.html',context)




def assignment_details(request, pk):
    view_all_applicants=True
    try: 
          assignment= Assignment.objects.get(id=pk)
          return render(request, 'Assignment/assignment-details.html',
                         {
                        'assignment_found': True,
                        'assignment': assignment ,
                        'view_applicants':view_all_applicants}
                        )
                                       
    except Exception as exc:
         print(exc)
         return render(request, 'Assignment/assignment-details.html',
                  { 'assignment_found': False
                   })




def registration_confirmation(request):
    return render(request, 'Assignment/registration-success.html')


