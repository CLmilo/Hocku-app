from os import terminal_size
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
# Create your views here.


def login(request):

    return render(request,'login.html')