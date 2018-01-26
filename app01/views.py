from django.shortcuts import render

# Create your views here.

def  index(request):
    return  render(request,'index.html')


def sales(request):
    return render(request,'sales/sales.html')
def customer(request):
    return render(request,'sales/customers.html')