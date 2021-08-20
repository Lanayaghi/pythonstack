from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    book = models.ManyToManyField(Books, related_name="Author")
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
def addOneBook(title, desc):
    new_book = Books.objects.create(title = title, desc = desc)
    return new_book

def allbooks():
    return Books.objects.all()

def getbooks (id):
    return Books.objects.get(id = id)
    
def allauthers():
    return Authors.objects.all()

def addOneAuthor(first_name, last_name, notes):
    new_author = Authors.objects.create(first_name = first_name, last_name = last_name, notes = notes)
    return new_author

def getauthors (id):
    return Authors.objects.get(id = id)
