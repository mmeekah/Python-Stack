# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.index),
    path('users', views.add_user)
]
