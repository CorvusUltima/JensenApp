
from django.contrib.auth.models import  User
from django.db import models
import uuid



# Create your models here.
class Profile(models.Model):      
     user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     email = models.EmailField()
     profile_picture= models.ImageField(null=True,blank= True,default="user-default.png")
     bio = models.TextField(max_length=1000,blank=True)
     created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
     id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
     @property
     def fullname(self):
        if self.first_name:
           return f"{self.first_name} {self.last_name}"
        return "missing name"

     def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
   