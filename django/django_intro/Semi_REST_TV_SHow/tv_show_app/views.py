from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def home_page(request):
    return redirect('/shows')

def index(request):
    context={
        'all_shows': Show.objects.all()
    }
    return render(request, 'index.html',context)



def create_show(request):

    return render(request, 'new_show.html')



def show_profile(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context ={
        'show': this_show
    }

    return render(request, 'show_profile.html', context)

def show_edit(request, show_id):
    context ={
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit_profile.html', context)

def update_profile(request,show_id):
    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.r_date = request.POST['release_date']
    show.desc = request.POST['desc']
    show.save()

    return redirect(f"/shows/{show_id}")

def add_show(request):
    new_show = Show.objects.create(
        title=request.POST['title'], 
        network=request.POST['network'],
        r_date=request.POST['release_date'], 
        desc=request.POST['desc'])
    return redirect('/shows')

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')

