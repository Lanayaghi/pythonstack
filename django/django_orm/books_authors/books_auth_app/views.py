# from django.http import request
from . models import Books, Authors
from django.shortcuts import redirect, render

def index(request):
    context = {
        'books' : Books.objects.all(),
        'authors' : Authors.objects.all(),
        
        }
    return render(request,'index.html', context)

def book(request):
    
    # title = request.POST['title']
    # desc = request.POST['desc']

    Books.objects.create( title = request.POST['title'], desc = request.POST['desc'])
    
    
    return redirect ('/')