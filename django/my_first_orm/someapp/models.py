from django.db import models


    
class student(models.Model):
    name = models.CharField(max_length=45)
    address = models.TextField()
    birthdy = models.DateTimeField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

