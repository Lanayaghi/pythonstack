from django.shortcuts import redirect, render
from . models import user
from . import models

def index(request):
    context = {
        'ALLusers': user.objects.all()
    }
    return render(request, 'tabel.html', context)

def new(request):
    if request.method == 'POST':
        user.objects.create(first_name=request.POST['first'], last_name=request.POST['last'],  email=request.POST['email'], age=request.POST['age'])
    return redirect('/')