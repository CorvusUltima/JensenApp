
from django.contrib.auth.models import  User
from django.db import models
from django.db.models.fields.related import OneToOneField



# Create your models here.
class Profile(models.Model):
     user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
     first_name=models.CharField(max_length=100)
     last_name=models.CharField(max_length=100)
     email=models.EmailField()
     profile_picture=models.ImageField(null=True,blank= True,default="user-default.jpg")
     bio=models.CharField(max_length=100)
    

   
     def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"



 