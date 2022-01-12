import uuid
from django.db import models
from django.contrib.auth.models import User





# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=300)
    def __str__(self):
       return f"{self.name} {self.adress}"

class Applicant(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE ,null=True)

    def __str__(self):
        profile = self.owner.profile
        return f"{profile.first_name} {profile.last_name} - {profile.email}"

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
       return self.name

class Assignment(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    title = models.CharField(max_length=200)
    featured_picture = models.ImageField(null=True,blank=True , default = "project.jpg")
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True,blank=True)
    applicant = models.ManyToManyField(Applicant)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return f"{self.title} {self.location}"
    
