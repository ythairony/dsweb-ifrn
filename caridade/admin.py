from django.contrib import admin
from .models import Evento, Item, Reserva

admin.site.site_header = 'EVENTO DE CARIDADE'

admin.site.register(Evento)
admin.site.register(Item)
admin.site.register(Reserva)
