from django.urls import path     
from . import views

urlpatterns = [
    path('', views.game),
    path('root', views.guess),
    path('path', views.playagain)
]