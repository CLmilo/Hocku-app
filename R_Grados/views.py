from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View   
# Create your views here.

def RViews(request):

    return render(request,'index.html')


'''
def RViews(View):
    template_name = 'index.html'
    return render(template_name)
'''