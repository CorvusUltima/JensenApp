from django.shortcuts import render
from .models import Assignment

# Create your views here.

def index(request):
   
    assignments = Assignment.objects.all()

    return render(request, 'assignment/index.html',
                  {'isActive': True, 'assignments': assignments})


def assignment_details(request, assignment_slug):
   try:
        assignment= Assignment.objects.get(slug=assignment_slug)

        return render(request, 'assignment/assignment-details.html',
                  {    'assignment_found': True,
                      'assignment_title': assignment.title,
                      'assignment_description': assignment.description
                   })
   except Exception as exc:
        return renderd(request, 'assignment/assignment-details.html',
                  { 'assignment_found': False,
                   
                   })
