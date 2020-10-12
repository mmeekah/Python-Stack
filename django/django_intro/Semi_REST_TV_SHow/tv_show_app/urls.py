from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('shows', views.index),
    path('shows/new', views.create_show),
    path('shows/create', views.add_show),
    path('shows/edit/<show_id>', views.show_edit),
    path('shows/edit/<show_id>/update', views.update_profile),
    path('shows/<show_id>', views.show_profile),
    path('shows/<show_id>/destroy', views.destroy),
    


]