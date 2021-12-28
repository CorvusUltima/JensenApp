from django.forms import ModelForm
from .models import Profile


class CreateProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude = ('user','assignments')

    def __init__(self,*args,**kwargs):
        super(CreateProfileForm, self).__init__(*args,**kwargs)
    
        for _,field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})




          
	