from django.shortcuts import redirect, render, HttpResponse

def show(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    return render(request, 'counter.html')


def reset(request):
    request.session.clear()
    return redirect('/')


