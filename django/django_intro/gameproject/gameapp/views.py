from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import random


def game(request):
    request.session['number'] = random.randint(1, 100)
   
    context = {
        'color' : '',
        'status' : ''
    }
    
    return render(request, "game.html", context)

def guess(request):
    print(request.POST['num'])
    if int(request.POST['num']) == request.session['number']:
        context = {
        'color' : 'green',
        'status' : 'congrats',
        }
        
        return render(request,'game.html', context)
    elif int(request.POST['num']) > request.session['number']:
        context = {
        'color' : 'red',
        'status' : 'too high',
        }
        return render(request,'game.html', context)

    elif int(request.POST['num']) < request.session['number'] :
        context = {
        'color' : 'red',
        'status' : 'too low',
        }
        return render(request,'game.html',context)

    return redirect('/')

def playagain(request):
    return render(request,'game.html')
