from django.contrib.messages.api import success
from django.shortcuts import redirect, render, HttpResponse
from . models import *
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
        return redirect('/success')
    
    messages.error(request, 'incorrect email address or password')
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        messages.error(request, 'please login ')
        return redirect('/')
    return render(request, 'success.html')
    
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