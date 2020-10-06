from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return (request, "index.html")

def create_counter(request):
    
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1

    context = {
        "count":request.session['count']
    }
    return render(request, 'index.html',context )

def destroy_session(request):
    request.session.clear()
    return redirect('/')

def increment(request):
    
    if 'increment' not in request.session:
        request.session['increment'] = 0
    request.session['increment'] += 2
    context = {
        "increment":request.session['increment']
    }   
    return render(request, 'index.html', context)


