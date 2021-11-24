from django import forms

class RegistrationForm(forms.Form):
	email = forms.EmailField(label ='your email')
	first_name =forms.CharField(label ='your first name', max_length =200)
	last_name =forms.CharField(label ='your last name', max_length =200)