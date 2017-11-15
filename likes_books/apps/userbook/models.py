# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    first_name= models.CharField(max_length= 255)
    last_name= models.CharField(max_length= 255)
    email=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Books(models.Model):
    name = models.CharField(max_length= 255)
    desc = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_users = models.ManyToManyField(Users, related_name="liked_books")
    uploader=models.ForeignKey(Users, related_name="uploaded_books")

# Create your models here.
