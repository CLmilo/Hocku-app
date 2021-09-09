from typing import Match
from django.db import models
from datetime import date, datetime
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from GestionPersonas.models import Party,Usuario

# Create your models here.

class Tienda(models.Model):
    id_tienda = CharField(max_length=12, primary_key=True)
    id_party = ForeignKey(Party,on_delete=models.CASCADE)
    nombre = CharField(max_length=1500,blank=True,null=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    referencia = CharField(max_length=1500,blank=True,null=True)
    direccion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)

class Tienda_Encargado(models.Model):
    id_tienda = ForeignKey(Tienda,on_delete=models.CASCADE)
    id_user = ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha_inicio = DateField(default=timezone.now,null=True,blank=True)
    fecha_fin = DateField(null=True,blank=True)

class Tipo_Producto(models.Model):
    id_tipo_prod = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    

class Estado_Producto(models.Model):
    id_est_prod = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    


class Medida(models.Model):
    id_medida = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    

class Conversion(models.Model):
    id_medida1 = CharField(max_length=6,primary_key=True)
    id_medida2 = CharField(max_length=6)
    factor = IntegerField(null=True,blank=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)

    class Meta:
        unique_together = (('id_medida1','id_medida2'),)


class Categoria(models.Model):
    id_categoria = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    

class Producto(models.Model):
    id_producto = IntegerField(auto_created=True, primary_key =True)
    id_tienda = ForeignKey(Tienda,on_delete=models.CASCADE)
    id_tipo_prod = ForeignKey(Tipo_Producto,on_delete=models.CASCADE)
    id_est_prod =  ForeignKey(Estado_Producto,on_delete=models.CASCADE)
    id_medida =ForeignKey(Medida,on_delete=models.CASCADE)
    id_categoria =ForeignKey(Categoria,on_delete=models.CASCADE)

class Complemento(models.Model):
    id_producto = ForeignKey(Producto,on_delete=models.CASCADE)
    id_producto = ForeignKey(Producto,on_delete=models.CASCADE)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    

class Estado_Caracteristica(models.Model):
    id_est_carac = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    

class Tipo_Caracteristica(models.Model):
    id_tipo_carac = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    


class Caracteristica(models.Model):
    id_caracteristica = CharField(max_length=12, primary_key=True)
    id_tipo_carac = ForeignKey(Tipo_Caracteristica,on_delete=models.CASCADE)
    id_est_carac =  ForeignKey(Estado_Caracteristica,on_delete=models.CASCADE)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)       

class Estado_Precio(models.Model):
    id_est_pre = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    

class Tipo_Precio(models.Model):
    id_tipo_pre = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)    

class Moneda(models.Model):
    id_moneda = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)  

class Conversion_Moneda(models.Model):
    id_moneda1 = CharField(max_length=6,primary_key=True)
    id_moneda2 = CharField(max_length=6)
    factor = FloatField(null=True,blank=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)

    class Meta:
        unique_together = (('id_moneda1','id_moneda2'),)


class Sobre_Costo(models.Model):
    id_sobrecosto = CharField(max_length=6, primary_key=True)
    monto = FloatField(blank=True,null=True)
    rangomin = FloatField(blank=True,null=True)
    rangomx = FloatField(blank=True,null=True)
    fecha_fin = DateField(null=True,blank=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)      

class Componente_Costo(models.Model):
    id_precio = CharField(max_length=12, primary_key=True)
    id_est_pre = ForeignKey(Estado_Precio,on_delete=models.CASCADE)
    id_tipo_pre = ForeignKey(Tipo_Precio,on_delete=models.CASCADE)
    id_moneda = ForeignKey(Moneda,on_delete=models.CASCADE)
    id_producto = ForeignKey(Producto,on_delete=models.CASCADE,null=True,blank=True )
    id_caracteristica = ForeignKey(Caracteristica,on_delete=models.CASCADE,null=True,blank=True)
    id_sobrecosto = ForeignKey(Sobre_Costo,on_delete=models.CASCADE)
    descripcion = CharField(max_length=1500,blank=True,null=True)
    valor =  FloatField()
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)   


