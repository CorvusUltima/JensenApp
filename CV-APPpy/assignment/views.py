from django.shortcuts import render
from .models import Assignment

# Create your views here.

def index(request):
   
    assignments = Assignment.objects.all()

    return render(request, 'assignment/index.html',
                  {'isActive': True, 'assignments': assignments})


def assignment_details(request, slug):
    print(assignment_slug)
    assignment_selected = {
        'title': slug + " assignment",
        'description': 'just some empty hard coded data for testing '
    }

    return render(request, 'assignment/assignment-details.html',
                  {'assignment_title': assignment_selected['title'],
                   'assignment_description': assignment_selected['description']
                   })
