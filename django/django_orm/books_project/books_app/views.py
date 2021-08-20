from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . import models
from books_app.models import *
def index(request):
    context = {
        'books' : allbooks()
    }
    return render( request, 'index.html', context)

def addbook(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        newly_created_book = addOneBook(title, desc)
        return redirect('/')
    
def showbook(request, id):
    
    context = {
        'thisbook' :  getbooks(id),
        'allauthors' : allauthers()
    }
    return render(request, 'show.html', context)

def AddAuthorToBook(request, book_id):
    if request.method == 'POST':
        
        selecte_author_id =  request.POST['selected_auther']
        selected_author = Authors.objects.get(id = selecte_author_id)
        this_book = Books.objects.get(id = book_id)
        this_book.Author.add(selected_author)
        return redirect ('/AddAuthorToBook/'+str(book_id))
    return redirect('/shows/'+str(book_id))

def Adauthor(request):
    context = {
        'authors' : Authors.objects.all()
    }
    if request.method == 'POST':
        first_name = request.POST['FirstName']
        last_name = request.POST['LastName']
        notes = request.POST['notes']
        newly_created_author = addOneAuthor(first_name, last_name, notes)
    return render (request, 'author.html', context)


def showauthor(request, id):
    
    context = {
        'thisauthor' :  getauthors (id),
        'books' : allbooks()
    }
    return render(request, 'showbook.html', context)

def Book(request, author_id):
    if request.method == 'POST':
        selected_book_id=  request.POST['book']
        book= Books.objects.get(id =  selected_book_id)
        this_author = Authors.objects.get(id = author_id)
        this_author.book.add(book)

    return redirect('/authors/'+str(this_author.id))