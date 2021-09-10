from Apps.GestionPersonas.models import Persona
from os import terminal_size
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
# Create your views here.
# ! from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView, DetailView, TemplateView
from django.views.generic import View   

'''def login(request):

    return render(request,'login.html')
'''

class PersonasView(View):
    model = Persona
    template_name = 'index.html'
    