from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.create_counter),
    path('',views.destroy_session),
    path('increment', views.increment),
    # path('increment', views.create_counter),
    path('clear', views.destroy_session),

    
    
    
]