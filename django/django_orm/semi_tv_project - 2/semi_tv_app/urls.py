from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new' , views.new),
    path('shows/add', views.add),
    path('delete/<int:id>', views.delete),
    path('show/<int:id>', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    
]