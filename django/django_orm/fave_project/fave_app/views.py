from django.contrib.messages.api import success
from django.shortcuts import redirect, render, HttpResponse
from . models import *
from . import models

from django.contrib import messages
import bcrypt

def index(request):
    return render(request,"index.html")

def register(request):
    
    errors = Users.objects.validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode() 
        Users.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        messages.info(request, 'you are now registerd!please login')
    return redirect ('/')

def login(request):
    try:
        user = Users.objects.get(email = request.POST['email'])
    except:
        messages.error(request, 'incorect email address or password')
        redirect('/')
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['user_id'] = user.id
        request.session['user_first_name'] = user.first_name
        request.session['user_last_name'] = user.last_name
        request.session['user_email'] = user.email
        return redirect('/welcome')
    
    messages.error(request, 'incorrect email address or password')
    return redirect('/')

def welcome(request):
    if 'user_id' not in request.session:
        messages.error(request, 'please login ')
        return redirect('/')
    context = {
        'all_books' : models.get_all_books(),
        'fave_books' : models.get_all_faves(request.session['user_id'])
        }
     
    return render(request, 'books.html',  context)
    
def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_first_name' in request.session:
        del request.session['user_first_name']
    if 'user_last_name' in request.session:
        del request.session['user_last_name']
    if 'user_email' in request.session:
        del request.session['user_email']
    return redirect('/')

def books(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        models.create_book(title, desc, request.session['user_id'])
        return redirect('/welcome')
    return redirect('')

def add_fave(request, book_id):
    if 'user_id'  in request.session:
        models.add_fave_book(request.session['user_id'], book_id)
        return redirect('/welcome')
    redirect('/')
    
def add_book(request, user_id):
      if request.session['user_id']:
        
        return render(request, 'book1.html')
  