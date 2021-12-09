from django.forms import ModelForm
from .models import Applicant
from .models import Assignment

class RegistrationForm(ModelForm):
    class Meta:
        model=Applicant
        fields='__all__'


class AssignmentForm(ModelForm):
    class Meta:
        model=Assignment
        fields='__all__'



          
	