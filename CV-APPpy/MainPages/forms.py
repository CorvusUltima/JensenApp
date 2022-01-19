"""
Definition of forms.
"""

from django import forms
from .models  import Room
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import  User
from django.utils.translation import ugettext_lazy as _


# This bugged out the registration for badly for some weird reason, it forced it to use "username" and "password" only whenever you wanted to have a custom form.
#class BootstrapAuthenticationForm(AuthenticationForm):
#    """Authentication form which uses boostrap CSS."""
#    username = forms.CharField(max_length=254,
#                               widget=forms.TextInput({
#                                   'class': 'form-control',
#                                   'placeholder': 'User name'}))
#    password = forms.CharField(label=_("Password"),
#                               widget=forms.PasswordInput({
#                                   'class': 'form-control',
#                                   'placeholder':'Password'}))


# This could be usefull in the future if we want to add more information to e.g also add email to the registration form.
class RegistrationForm(AuthenticationForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))
    #email = forms.EmailField(max_length=60, help_text='Required: Add a valid email address')
    class Meta:
        model = User 
        fields = ("username", "password1", "password2")# "password", "password_two")
    
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields='__all__'
    