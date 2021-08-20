from django.shortcuts import redirect, render, HttpResponse
from user_auth_app.models import Users

def index(request):
    if 'user' in request.session:
        return redirect('/welcome')
    return render(request,'index.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    address = request.POST['address']
    user = Users.objects.create(username = username, password = password , address = address , email = email)
    data = {
        'username' : username, 
        'password' : password, 
        'email'  : email,
        'address' : address
    }
    request.session['user']= data
    return redirect('/welcome')

def welcome(request):
    if 'user' in  request.session: 
        user = request.session['user'] 
        return render(request, 'welcome.html', user)
    return redirect('/')

def logout(request):
    if 'user' in  request.session:
        request.session.clear()
    return redirect('/')  

