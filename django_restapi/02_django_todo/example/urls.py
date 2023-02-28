from django.urls import path, include
from .views import HelloAPI, BookAPI, BooksAPI, bookAPI, booksAPI

urlpatterns = [
    path('hello/', HelloAPI),
    path("fbv/books/", booksAPI),  # FBV
    path('fbv/book/<int:bid>/', bookAPI),  # FBV    
    path("cbv/books/", BooksAPI.as_view()),  # CBV
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
]




