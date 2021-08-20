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
    path("thought/<int:user_id>" , views.details)
   
]