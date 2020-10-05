from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def first_view(request):
    return redirect("/blogs")

def second_view(request):
    return HttpResponse("This method is the second view in app_one")

