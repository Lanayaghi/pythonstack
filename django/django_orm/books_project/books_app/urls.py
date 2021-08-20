from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook', views.addbook),
    path ('shows/<int:id>', views.showbook),
    path('AddAuthorToBook/<int:book_id>' , views.AddAuthorToBook),
    path('AddAuthor', views.Adauthor),
    path('authors/<int:id>', views.showauthor), 
    path ('AddBookTAuthor/<int:author_id>', views.Book)
]