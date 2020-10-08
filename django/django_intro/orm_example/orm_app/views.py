from django.shortcuts import render
from orm_app.models import *

def index(request):
    context = {
        "all_stars" : Star.objects.all()
    }
    return render(request,'index.html',context)
    