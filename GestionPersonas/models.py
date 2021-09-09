from django.db import models
from datetime import date, datetime
from django.db.models.fields import CharField, DateField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# Create your models here.

class Party(models.Model):
    id_party = CharField(max_length=12, primary_key=True)
    tipo_party = CharField(max_length=200,null=True,blank=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)
    

class Persona(models.Model):
    id_party = ForeignKey(Party,on_delete=models.CASCADE, primary_key=True)
    dni = CharField(max_length= 8)
    nombres = CharField(max_length=1500)
    apellidos = CharField(max_length=1500)
    sexo = CharField(max_length=200)
    fecha_nacimiento = DateField()
    

class Organizacion(models.Model):
    id_party = ForeignKey(Party,on_delete=models.CASCADE, primary_key=True)
    ruc = CharField(max_length=11)
    nombre = CharField(max_length=1500)
    giro_comercial = CharField(max_length=200)
    
    
class Rol(models.Model):
    id_rol = CharField(max_length=12, primary_key=True)
    tipo_rol = CharField(max_length=200)
    descripcion = CharField(max_length=1500)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)


class Estado_Rol(models.Model):
    id_est_rol = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)


class Rol_Party(models.Model):
    id_rol_party = IntegerField(primary_key=True, auto_created=True)
    id_party = ForeignKey(Party,on_delete=models.CASCADE)
    id_rol = ForeignKey(Rol,on_delete=models.CASCADE)
    id_est_rol = ForeignKey(Estado_Rol,on_delete=models.CASCADE)
    fecha_inicio = DateField(default=timezone.now,null=True,blank=True)
    fecha_fin = DateField(null=True,blank=True)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)


class Estado_Mecanismo(models.Model):
    id_estado_mec = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)


class Tipo_Mecanismo(models.Model):
    id_tipo_mec = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)


class Mecanismo_Contacto(models.Model):
    id_mec_cont = CharField(max_length=12, primary_key=True)
    id_party = ForeignKey(Party,on_delete=models.CASCADE)
    id_tipo_mec = ForeignKey(Tipo_Mecanismo,on_delete=models.CASCADE) 
    id_estado_mec = ForeignKey(Estado_Rol,on_delete=models.CASCADE)     
    descripcion = CharField(max_length=1500)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)


class Tipo_Usuario(models.Model):
    id_tipo_user = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)


class Estado_Usuario(models.Model):
    id_est_user = CharField(max_length=6, primary_key=True)
    descripcion = CharField(max_length=1500)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)   


class Usuario(models.Model):    
    id_user = CharField(max_length=12, primary_key=True)
    id_party = ForeignKey(Party,on_delete=models.CASCADE)
    id_tipo_user = ForeignKey(Tipo_Usuario,on_delete=models.CASCADE)
    id_est_user = ForeignKey(Estado_Usuario,on_delete=models.CASCADE)
    username = CharField(max_length=200,null=True, blank=False)
    pass_word = CharField(max_length=200, null=True, blank=False)
    user_creacion = CharField(max_length=12,null=True,blank=True)
    fecha_creacion  = DateField(default=timezone.now,null=True,blank=True)
    user_actualizacion = CharField(max_length=12,null=True,blank=True)
    fecha_actualizacion = DateField(null=True,blank=True)   
