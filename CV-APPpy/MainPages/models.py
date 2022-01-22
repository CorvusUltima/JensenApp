"""
Definition of models.
"""

from pyexpat import model
from tkinter import CASCADE
from django.db import models
from ProfilePages.models import Profile
import uuid
from django.contrib.auth.models import  User



# Create your models here.


class Topic(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):      
    host = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    topic= models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated=  models.DateTimeField(auto_now=True ,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
   
    def __str__(self):
        return f"{self.name}"

class Message(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,)
    room =models.ForeignKey(Room,on_delete=models.CASCADE,)
    body=models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated=  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]
