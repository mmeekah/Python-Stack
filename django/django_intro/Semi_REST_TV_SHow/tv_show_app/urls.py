from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('shows', views.index),
    path('shows/new', views.new),
    path('shows/create', views.add_show),
    path('shows/<show_id>/edit', views.show_edit),
    path('shows/<show_id>/update', views.update_profile),
    path('shows/<show_id>', views.show_profile),
    path('shows/<show_id>/destroy', views.destroy),
    


]