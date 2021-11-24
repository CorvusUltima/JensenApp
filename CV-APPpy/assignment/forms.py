from django import forms

from .models import Applicant

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Applicant
		fields = [ 'email', 'first_name', 'last_name' ]