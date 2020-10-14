from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signin', views.signin),
    path('registration', views.registration),
    path('register', views.register),
    path('login', views.login),
    path('admin_dashboard', views.admin_dashboard),
    path('user_dashboard', views.user_dashboard),
    path('admin_edit/<id>', views.admin_edit),
    path('admin_edit_info/<id>', views.admin_edit_info),
    path('user_edit/<id>', views.user_edit),
    path('user_edit_info/<id>', views.user_edit_info),
    path('user_edit_password', views.user_edit_password),
    path('show/<id>', views.show),
    path('message/<id>', views.message),
    path('add', views.add),
    path('admin_add', views.admin_add),
    path('delete/<id>', views.delete),
    path('logout', views.logout),
    # path('post_message/<user_id>', views.post_message),
    # path('post_comment', views.post_comment),
    # path('delete_message', views.delete_message)
    

]