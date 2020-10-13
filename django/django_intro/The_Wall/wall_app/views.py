from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *
from datetime import datetime, timedelta




# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        user = User.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'],
            email=request.POST['email'], 
            password=pw_hash,
        )
        request.session['uid'] = user.id
        return redirect('/wall')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['uid'] = logged_user.id
            return redirect('/wall')
        else:
            messages.error(request, "Wrong password")
    return redirect('/')



def wall(request):
    
    within_30_minutes = datetime.now() - timedelta(seconds=60 * 30)
    messages_before_30_mintues = Message.objects.filter(created_at = within_30_minutes)
    print(messages_before_30_mintues)
    if 'uid' not in request.session:
        messages.error(request, "You have not logged in or registered, please log in or register.")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['uid']),
        'all_messages': Message.objects.all(),
        'comments': Comment.objects.all()
    }
    return render(request, 'wall.html', context)


def post_message(request, user_id):
    errors = Message.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    else:
        user =  User.objects.get(id = user_id)
        Message.objects.create(message = request.POST['message'], user=user)
        return redirect('/wall')

def post_comment(request):
    errors = Comment.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    else:
        user = User.objects.get(id=request.POST['user_id'])
        message = Message.objects.get(id=request.POST['message_id'])
        Comment.objects.create(
            comment=request.POST['comment'], message=message, user=user)
        return redirect('/wall')

def delete_message(request):
    message_to_be_deleted = Message.objects.get(
        id=request.POST['delete_message_id'])
    message_to_be_deleted.delete()
    return redirect('/wall')

def logout(request):
    request.session.clear()
    messages.error(request, "You have successfully logged out.")
    return redirect('/')