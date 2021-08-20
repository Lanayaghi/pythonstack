from django.urls import path 
from . import views
urlpatterns = [
    path('', views.show),
    path('reset', views.reset)
    
    
]