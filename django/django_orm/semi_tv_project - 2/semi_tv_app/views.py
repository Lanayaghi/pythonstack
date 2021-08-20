from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from semi_tv_app.models import *

def index(request):
    
    return redirect('/shows')


def shows(request):
    context ={
        'shows': Shows.objects.all()
    }
    return render(request,'tv.html',context)

def new(request):
    return render(request ,'add.html')

def add(request):
    
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
                    
    else:
        title=request.POST['title']
        network = request.POST['network']
        date = request.POST['relearsdate']
        descripition = request.POST['desc']
        Shows.objects.create(title=title,network=network, release_date = date , descriptiont = descripition)
        return redirect('../')

def delete(request,id):
    x=Shows.objects.get(id=id)
    x.delete()
    return redirect('../')

def show (request, id):
    y=Shows.objects.get(id=id)
    context = {
        'show': y
    }
    return render(request,"show.html",context)

def edit(request, id):
    l = Shows.objects.get(id=id)
    context = {
        'show' : l
    }
    
    return render (request, 'edit.html' , context)

def update(request,id):
    #print(request.POST['title'])
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/update/'+ str(id))
    x = Shows.objects.get(id=id)
    x.title=request.POST['title']
    x.network = request.POST['network']
    x.descriptiont = request.POST['desc']
    if request.POST['relearsdate']:
        x.release_date = request.POST['relearsdate']
        x.save()
    return redirect('../update/<int:id>')



