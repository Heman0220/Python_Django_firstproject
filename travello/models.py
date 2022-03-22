from distutils.command import upload
from django.db import models
from numpy import imag

# Create your models here.

class destination(models.Model):

    name = models.CharField(max_length=100)
    dest = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

class location(models.Model):

    location =  models.CharField(max_length=100)
    location_details=models.TextField()

