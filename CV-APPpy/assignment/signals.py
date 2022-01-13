from django.db.models.signals import post_save ,post_delete

from django.contrib.auth.models import User
from ProfilePages.models import Skill
from assignment.models import Applicant, Tag

def is_unique(skill: Skill) -> bool:
    print('INSIDE IS_UNIQUE FUNCTION')
    try:
        Skill.objects.get(name__iexact = skill.name)
    except Skill.DoesNotExist:
        print('UNIQUE')
        return True
    except Skill.MultipleObjectsReturned:
        print("MULTIPLE")
        pass
    print('NOT UNIQUE')
    return False


def create_skill(sender, instance,created,**kwargs):
    print('INSIDE CREATE_SKILL SIGNAL')
    if created:
        tag= instance
        skill=Skill()
        skill.name=tag.name.strip()
        if is_unique(skill):
            print('creating new skill')
            skill.save()
    else:
        print('matching skill is aviable')
            

def delete_applicant(sender,instance,**kwargs):
    applicant=instance.applicant
   
    if applicant is not None:
        
        print('applicant Deleted')
    
    print('applicant is NONE')




post_save.connect(create_skill, sender=Tag)
post_delete.connect(delete_applicant,sender=Applicant)
