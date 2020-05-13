from django.urls import path 
from timiolarryscrumy import views 




urlpatterns = [ 
    path('', views.get_grading_parameters, name = 'get_grading_parameters'),
]