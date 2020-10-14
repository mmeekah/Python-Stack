from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('books', views.books),
    path('logout', views.logout),
    path('add_book/<user_id>', views.add_book),
    path('books/<book_id>', views.book_profile),
    path('edit_book/<book_id>', views.edit_book),
    path('delete_book<book.id>', views.delete_book),
    path('unfavorite/<book_id>/<user_id>', views.unfavorite),
    path('add_to_favorites/<book_id>/<user_id>', views.add_to_favorites),
    path('favorite_books', views.favorite_books)

    
]
