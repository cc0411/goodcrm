# -*- coding:utf-8 -*-

from django.conf.urls import url,include
from app01 import  views
urlpatterns = [
    url(r'customer/',views.customer,name='customer_list'),
    url(r'sales/',views.sales,name='sales_index'),

    ]