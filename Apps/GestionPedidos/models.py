from Apps.GestionProductos.models import Producto, Tienda
from typing import Match
from django.db import models
from datetime import date, datetime
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField, DateTimeField, IntegerField, FloatField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from Apps.GestionPersonas.models import Party,Usuario
# Create your models here.

from django.db import connection


def my_custom_sql(self, p_id_ticket):
    with connection.cursor() as cursor:
        cursor.execute("select coalesce(max(valor),1)from public.\"GestionPedidos_ticket_producto\" where id_ticket = %s" % p_id_ticket )
        row = cursor.fetchall()
    return row+1


class Estado_Ticket(models.Model):
    id_est_ticket = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    


class Tipo_Ticket(models.Model):
    id_tipo_ticket = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    
   

class Ticket(models.Model):
    id_tienda = CharField(max_length=12, primary_key=True)
    id_user = ForeignKey(Usuario,on_delete=models.CASCADE)
    id_user = ForeignKey(Usuario,on_delete=models.CASCADE, blank=True,null=True,name="recepcionista")
    id_tienda = ForeignKey(Tienda,on_delete=models.CASCADE)
    id_est_ticket = ForeignKey(Estado_Ticket,on_delete=models.CASCADE, blank=True,null=True)
    id_tipo_ticket = ForeignKey(Tipo_Ticket,on_delete=models.CASCADE, blank=True,null=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    monto_total = FloatField(blank=True,null=True)
    fecha_compra = DateTimeField(blank=True,null=True)
    fecha_entrega_estimada = DateTimeField(blank=True,null=True)
    fecha_entrega = DateTimeField(blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True, default='USR-0000001')
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    
      

class Ticket_Producto(models.Model):
    id_prod_ticket  = IntegerField(auto_created=True, primary_key=True)
    id_producto = ForeignKey(Producto,on_delete=models.CASCADE)
    secuencia = IntegerField() 
    id_ticket =  ForeignKey(Ticket,on_delete=models.CASCADE)
    p_unitario = IntegerField()
    cantidad = IntegerField(default=1)
    comentario = CharField(max_length=1500,blank=True,null=True)
    
