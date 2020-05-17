from django.conf.urls import url
#from django.urls import path
from timiolarryscrumy import views


urlpatterns = [ 
    url(r'', views.index, name = 'index'),
    #url(r'^/move_goal/(?P<poll_id>\d+)/$', views.move_goal, name = "move_goal"),
    #r'^(?P<pk>\d+)/$'
    url(r'^move_goal/(?P<pk>\d+)/$', views.move_goal, name = "move_goal"),
    #r'^move_goal/(\d+)/$'
]