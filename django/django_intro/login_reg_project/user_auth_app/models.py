from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    address = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)
    created_at =  models.DateTimeField(auto_now_add=True)