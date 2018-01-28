from django.shortcuts import render
from app01 import  models
# Create your views here.

def  index(request):
    column = models.Customer.objects.filter(id__gt=1)


    return  render(request,'index.html',{'column_list':column})


def sales(request):
    return render(request,'sales/sales.html')
def customer(request):
    return render(request,'sales/customers.html')