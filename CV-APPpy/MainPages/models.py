"""
Definition of models.
"""

from django.db import models
import uuid



# Create your models here.
class Room(models.Model):      
    #owner = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    #topic= 
    name = models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated=  models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
   
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
   
