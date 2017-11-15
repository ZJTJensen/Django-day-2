  # Inside models.py
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class dojos(models.Model):
    name = models.CharField(max_length=255)
    city= models.CharField(max_length= 255)
    state=models.CharField(max_length=255)
    def __repr__(self): 
        return "My name i {} i amd from {} in {}.".format(self.name, self.city, self.state)
class ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length= 255)
    dojos = models.ForeignKey(dojos, related_name = "ninjas")
    def __repr__(self): 
        return "My name i {} {}.".format(self.first_name, self.last_name)