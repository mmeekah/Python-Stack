from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book/create', views.add_book),
    path('author/create', views.add_author),
    path('book_to_author', views.add_book_to_author),
    path('book_dets/<book_id>', views.display_book_dets),
    path('author_dets/<auth_id>', views.display_author_dets),
    path('author_to_book', views.add_author_to_book)


]