from django.contrib import admin
from Apps.GestionProductos.models import Tienda,Producto,Caracteristica
# Register your models here.

admin.site.register(Tienda)
admin.site.register(Producto)
admin.site.register(Caracteristica)