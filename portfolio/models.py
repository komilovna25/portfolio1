from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django import forms

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
  
    
    def __str__(self):
        return self.name


class About(models.Model):
    image = models.ImageField(upload_to='Images/about')
    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=20) 

    def __str__(self):
        return self.name
class Portfolio(models.Model):
    image = models.ImageField(upload_to='Images/portfolio')
    title = models.CharField(max_length=70)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    


class Services(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Service_details(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Resume(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    

