from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context={
        'all_ninjas': Ninja.objects.all(),
        'all_dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)



def add_dojo(request):
    print(request.POST)
    
    new_dojo =Dojo.objects.create( 
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        state=request.POST['state'],
        desc=request.POST['desc'],
    )
    return redirect('/')


def add_ninja(request):
    print(request.POST)
    # How do I get the supplier object with just the id??
    dojos_id = request.POST['dojo']
    user_instance = Dojo.objects.get(id=dojos_id)
    # add item to DB
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo=user_instance
    )
    return redirect('/')