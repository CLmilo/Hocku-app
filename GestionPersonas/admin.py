from django.contrib import admin

from GestionPersonas.models import Party,Usuario,Persona,Organizacion
# Register your models here.

admin.site.register(Party)
admin.site.register(Usuario)
admin.site.register(Persona)
admin.site.register(Organizacion)