# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list
from myproject.myapp.views import index
from myproject.myapp.views import result



urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^$', index, name='index'),
    url(r'^result/$', result, name='result')
]
