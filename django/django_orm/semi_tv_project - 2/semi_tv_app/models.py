from django.db import models


class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print('im in the validator', postData['title'])
        if len(postData['title']) < 2:
            errors["title"] = "Blog title should be at least 2 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Blog network should be at least 3 characters"
        return errors

    
class Shows(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    descriptiont = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()
