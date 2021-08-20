from django.db import models
    
class Shows(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    descriptiont = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
