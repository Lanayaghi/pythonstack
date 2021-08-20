from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register', views.register),
    path('login', views.login),
    path('thoughts', views.thoughts),
    path('logout', views.logout),
    path('postCreation', views.post),
    path('delete/<int:id>', views.delete),
    path("thought/<int:id>" , views.details),
    path('add_like/<int:id>', views.add_liked),
    path('un_like/<int:id>', views.un_like)
   
]