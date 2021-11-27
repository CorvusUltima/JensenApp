from django.forms import ModelForm
from .models import Applicant

class RegistrationForm(ModelForm):
    class Meta:
        model=Applicant
        fields='__all__'


          
	