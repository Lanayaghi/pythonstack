from django.db import models
import re

class UsersManager(models.Manager):
    
    def validator(self, post_data):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name shouldve more than 2 charaters"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name shouldve more than 2 charaters"
        if not email_regex.match (post_data['email']):            
            errors['email'] = "Invalid email address!"
        try:
            self.get(email = post_data['email'])
            errors['email_unique'] = 'this email is already existed'
        except:
            pass
        if len(post_data['password']) <8 :
            errors['password'] = "password shouldve more than 8 charaters"
        if post_data['password'] != post_data['confirm']:
            errors['password_match'] = 'Password and confirm password should match.'
            
        return errors

class PostManager(models.Manager):
    def PostValidator(self, post_data):
        errors = {}
        if len(post_data['post']) < 5:
            errors['post'] = 'post should be more than 5 characters!'
        if len(post_data['post']) < 1:
            errors['post'] = 'Please Provide Your Post!'
        return errors
class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    password = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()

class Post(models.Model):
    post = models.CharField(max_length=45)
    user_post = models.ForeignKey(Users, related_name="user",on_delete = models.CASCADE)
    likes = models.ManyToManyField(Users, related_name="likes")
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()
    


    
def number_of_likes(self):
    return self.likes.count()

def get_all_likes(user_id):
    user = Users.objects.get(id = user_id)
    return user.likes.all 

def add__likes(post_id, user_id):
    user = Users.objects.get(id = user_id) 
    post = Post.objects.get(id = post_id)
