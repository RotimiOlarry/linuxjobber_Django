from django.urls import path 
from . import views  
from django.conf.urls import include 




urlpatterns = [ 
    path('', views.get_grading_parameters, name = 'get_grading_parameters'),
    ]