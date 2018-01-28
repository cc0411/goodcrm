from django.shortcuts import render
from kadmin import  kadmin_tables
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import  importlib
# Create your views here.


def index(request):
    return  render(request,'kadmin/index.html',{'table_list':kadmin_tables.enabled_admin})

def display_table_objs(request,app_name,table_name):
    #models_module = importlib.import_module('%s.models' %(app_name))
    #model_obj = getattr(models_module,table_name)
    admin_class = kadmin_tables.enabled_admin[app_name][table_name]
    object_list = admin_class.model.objects.all()
    paginator = Paginator(object_list, 2)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        query_sets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_sets = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_sets = paginator.page(paginator.num_pages)
    return  render(request,'kadmin/table_objs.html',{"admin_class":admin_class,"query_sets":query_sets})
