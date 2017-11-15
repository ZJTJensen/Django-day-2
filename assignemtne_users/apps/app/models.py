  # Inside models.py
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class app_users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length= 255)
    email_address=models.CharField(max_length=255)
    age=models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self): 
        return "I am {} {}. My email adress is {}. I am {} years old.".format(self.first_name, self.last_name, self.email_address, self.age)