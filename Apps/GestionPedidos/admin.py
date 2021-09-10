from Apps.GestionPedidos.models import Tipo_Ticket
from django.contrib import admin

from Apps.GestionPedidos.models import Ticket,Estado_Ticket,Tipo_Ticket  
# Register your models here.

admin.site.register(Ticket)
admin.site.register(Estado_Ticket)
admin.site.register(Tipo_Ticket)
