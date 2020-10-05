from django.shortcuts import render, HttpResponse

def first_view(request):
    return HttpResponse("This method is the first view in app_two")

def second_view(request):
    return HttpResponse("This methos is the second view in app_two")
# Create your views here.
