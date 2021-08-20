from django.shortcuts import render, redirect


def show(request):
    return render(request, 'survey.html')

def result(request):
    print(request.POST['name'])
    print("I am in line 9 ")
    request.session ['name1']=request.POST['name'] 
    request.session['location1'] = request.POST['location']
    request.session['fave'] = request.POST['fave']
    request.session['comment'] = request.POST['comment']
    
    
    
    return redirect('/trial')
    

def middle(request):
    
    
    return render(request, 'result.html')
