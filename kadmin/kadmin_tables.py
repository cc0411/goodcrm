# -*- coding:utf-8 -*-
from app01 import  models
#app名称enabled_admin
enabled_admin = {}
class BaseAdmin(object):
    list_display = []
    list_filter = []
    search_fields = []
    raw_id_fields = []
    filter_horizontal = []
    list_editable = []
    list_per_page = 2
class CustomerAdmin(BaseAdmin):
    list_display = ['qq','name','source','date']
    list_filter = ['qq','name','source','date']

class CourseAdmin(BaseAdmin):
    list_display = ('name','price')

#获取app名字  models.UserProfile._meta.app_label
#获取当前表名model_class._meta.model_name
#model_class 表名

def register(model_class,admin_class=None):
    if model_class._meta.app_label not in enabled_admin:
        enabled_admin[model_class._meta.app_label] = {} #enabled_admins['crm'] = {}
    #admin_obj = admin_class()
    admin_class.model = model_class #绑定model 对象和admin 类
    enabled_admin[model_class._meta.app_label][model_class._meta.model_name] = admin_class
    #enabled_admins['crm']['customerfollowup'] = CustomerFollowUpAdmin



register(models.Customer,CustomerAdmin)
register(models.Course,CourseAdmin)

















