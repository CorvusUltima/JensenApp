import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=300)
    def __str__(self):
       return f"{self.name} {self.adress}"

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
       return self.name

class Applicant(models.Model):
   first_name=models.CharField(max_length=100)
   last_name=models.CharField(max_length=100)
   email=models.EmailField(unique=True)
   

   def __str__(self):
    return f"{self.first_name} {self.last_name} - {self.email}"

class Assignment(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    tags = models.ManyToManyField(Tag,blank=True, null=True  )
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    applicant = models.ManyToManyField(Applicant,blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return f"{self.title} {self.location}"