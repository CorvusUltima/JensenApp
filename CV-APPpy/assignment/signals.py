from django.db.models.signals import post_save ,post_delete
from django.contrib.auth.models import User
from assignment.models import Applicant



def delete_applicant(sender,instance,**kwargs):
    applicant=instance.applicant
   
    if applicant is not None:
        
        print('applicant Deleted')
    
    print('applicant is NONE')




post_delete.connect(delete_applicant,sender=Applicant)
