# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('first-route/', views.first_view),
    path('second-route/', views.second_view),
]


# # from django.contrib import admin
# from django.urls import path
# from . import views
# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('first-route', views.first_view),
#     path('second-route/', views.second_view),
# ]