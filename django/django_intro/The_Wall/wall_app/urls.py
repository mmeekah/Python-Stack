from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wall', views.wall),
    path('logout', views.logout),
    path('post_message/<user_id>', views.post_message),
    path('post_comment', views.post_comment),
    path('delete_message', views.delete_message)
    

]