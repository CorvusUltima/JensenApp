from django.forms import ModelForm
from .models import Applicant
from .models import Assignment

class ApplicationForm(ModelForm):
    class Meta:
        model=Applicant
        fields='__all__'


class AssignmentForm(ModelForm):
    class Meta:
        model=Assignment
        fields='__all__'
        exclude = ('host', 'applicant')

        def __init__(self,*args,**kwargs):
            super(AssignmentForm, self).__init__(*args,**kwargs)
        
            for _,field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})
        
