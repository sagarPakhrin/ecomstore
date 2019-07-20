from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


# class 
def index(request):
    return render(request,'catalog/index.html',{})

def shop(request):
    return render(request,'shop.html')
