from django.shortcuts import render, redirect, HttpResponse
import random


def root(request):
    return redirect('/')

def set_number(request):
    if 'magic_number' not in request.session:
        request.session['magic_number'] = random.randrange(1, 101)
    print("Number is " + str(request.session['magic_number']))
    return render(request, "index.html")


def set_guess(request):
    magic_number = int(request.session['magic_number'])
    guess_number = int(request.POST['guess_num'])
    print(magic_number)
    print(guess_number)
    if magic_number == guess_number:
        request.session['result'] = 1
    elif magic_number > guess_number:
        request.session['result'] = 2
    elif magic_number < guess_number:
        request.session['result'] = 3
    return redirect('/')


def reset_game(request):
    request.session['magic_number'] = str(0)
    request.session['result'] = None
    return redirect('/')