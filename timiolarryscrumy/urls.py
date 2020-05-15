from django.conf.urls import url 
from timiolarryscrumy import views


urlpatterns = [ 
    url(r'^$', views.index, name = 'index'),
]