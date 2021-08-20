from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register', views.register),
    path('login', views.login),
    path('welcome', views.welcome),
    path('logout', views.logout),
    path('books', views.books),
    path('/add_fave/<int:id', views.add_fave),
    path('books/<int:id>', views.add_book)
]