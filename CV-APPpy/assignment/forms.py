from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Applicant, Tag
from .models import Assignment

class ApplicationForm(ModelForm):
    class Meta:
        model=Applicant
        fields='__all__'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields='__all__'
        exclude = ('owner',)




class AssignmentForm(ModelForm):
    class Meta:
        model=Assignment
        fields='__all__'
        exclude = ('host', 'applicant')

        def __init__(self,*args,**kwargs):
            super(AssignmentForm, self).__init__(*args,**kwargs)
        
            for _,field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})
        
