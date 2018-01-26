# -*- coding:utf-8 -*-

from django.conf.urls import url,include
from kadmin import  views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^/(\w+)/(\W+)',views.display_table_objs,name='table_objs')
    ]