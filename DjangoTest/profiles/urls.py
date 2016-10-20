# -*- coding: utf-8 -*-
'''
Created on 2016. 10. 20.

@author: swhong
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', views.profiles, name='profiles'),
]