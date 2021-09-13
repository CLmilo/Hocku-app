from hocku import view
from Apps.GestionPersonas import models
from Apps.GestionPersonas.models import Persona, Usuario
from os import terminal_size
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from django.db import connection

# Create your views here.
# ! from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView, DetailView, TemplateView
from django.views.generic import View   

'''def login(request):

    return render(request,'login.html')
'''

class Usuario_Do():
    def   __init__(self,id_usuario,username,psw,nombre,estado,tipo):
        self.id_usuario
        self.username 
        self.psw
        self.nombre
        self.estado
        self.tipo




def Login(request):

    v_name = request.GET["mail"]
    v_psw = request.GET["psw"]
    
    '''with connection.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM  public.\"GestionPersonas_usuario\" where username = %s and pass_word = %s", [v_name, v_psw])
        row = cursor.fetchone()
        '''
    respuesta = Usuario.objects.filter(username__exact = v_name,pass_word__exact = v_psw )
    print(v_name)
    print(respuesta)
    #v_usuario = Usuario.objects.raw("SELECT count(*) FROM  public.\"GestionPersonas_usuario\"")# where username = %s and pass_word = %s", [v_name, v_psw])
    return HttpResponse(respuesta)

    #return render(request,'index.html')



def Registro(request,self):

    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()


    render(request,'login.html')