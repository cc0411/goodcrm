from django.shortcuts import render
from kadmin import  kadmin_tables
# Create your views here.


def index(request):
    return  render(request,'kadmin/index.html',{'table_list':kadmin_tables.enabled_admin})

def display_table_objs(request,app_name,table_name):
    return  render(request,'kadmin/table_objs.html')
