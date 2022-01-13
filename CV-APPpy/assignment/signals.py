from django.db.models.signals import post_save ,post_delete

from django.contrib.auth.models import User
from ProfilePages.models import Skill
from assignment.models import Applicant, Tag

def create_skill(sender, instance,created,**kwargs):
        if created:
            tag= instance
            skill=Skill()
            skill.name=tag.name
            print('creating new skill')
            skill.save()
        else:
            print('matching skill is aviable')
            

def delete_applicant(sender,instance,**kwargs):
    applicant=instance.applicant
   
    if applicant is not None:
        
        print('applicant Deleted')
    
    print('applicant is NONE')

def delete_tag(sender,instance,**kwargs):
    print(' tag deleted ')


post_save.connect(create_skill, sender=Tag)
post_delete.connect(delete_tag,sender=Tag)
post_delete.connect(delete_applicant,sender=Applicant)
