from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=300)
    def __str__(self):
       adress=self.name+' '+ self.adress
       return adress

class Applicant(models.Model):
   first_name=models.CharField(max_length=100)
   last_name=models.CharField(max_length=100)
   email=models.EmailField(unique=True)
   
   def __str__(self):
    str= self.first_name 
    return str 

class Assignment(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL, null= True )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    applicant=models.ManyToManyField(Applicant,blank=True, null=True)
    # registrated user #
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        title=self.title+' '+ self.slug
        return title