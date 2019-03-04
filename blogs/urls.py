from django.conf.urls import url
from django.contrib import admin
from .views import *
urlpatterns = [	
	#url(r'^$', post_list,name='list'),
    url(r'^create/$', post_create),
    url(r'^list/$', post_list),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    
    
]