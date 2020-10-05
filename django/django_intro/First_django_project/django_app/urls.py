# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.root),
    path('blogs/', views.index),
    path('blogs/new/', views.new),
    path('blogs/create/', views.create),
    path('blogs/<int:number>/show', views.show),
    path('blogs/<int:number>/edit',views.edit),
    path('blogs/<int:number>/destroy', views.destroy),
    pat('blogs/json', views.json_file)
]

# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^new$', views.new),
#     url(r'^create$', views.create),
#     url(r'^(?P<number>\d+)$', views.show),
#     url(r'^(?P<number>\d+)/edit$', views.edit),
#     url(r'^(?P<number>\d+)/delete$', views.destroy),
# ]