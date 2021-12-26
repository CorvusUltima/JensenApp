from django.db.models.signals import post_save ,post_delete
from django.contrib.auth.models import User
from ProfilePages.models import Profile

def create_profile(sender, instance,created,**kwargs):
        if created:
            user= instance
            profile=Profile()
            profile.user=user
            profile.save()
        else:
            user_local= instance
            profile=Profile.objects.get(user=user_local)
            profile.first_name=user_local.first_name
            profile.last_name=user_local.last_name
            print(profile.user)
            print(profile.first_name)
            profile.save()


def delete_profile(sender,instance,**kwargs):
    user=instance.user
    if(user is not None):
        user.delete()
        print('User Deleted')
    
    print('user is NONE')



post_save.connect(create_profile, sender=User)

post_delete.connect(delete_profile,sender=Profile)

