from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse


def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f'placeholder to display blog number: {number}')

def edit(request, number):
    return HttpResponse(f'placeholder to display blog number: {number}')

def destroy(request, number):
    return redirect('/blogs')

def eshmabedi(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})

