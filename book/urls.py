from django.urls import path
from .views import home, books, authors, book_detail

urlpatterns = [
    path('', home, name='home'),
    path('books/', books, name='books'),
    path('authors/', authors, name='authors'),
    path('book/<slug:slug>/', book_detail, name='book-detail'),

]