from django.contrib import admin
from .models import Pergunta, Alternativa

admin.site.site_header = 'Enquetes'

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 2

class PerguntaAdmin(admin.ModelAdmin):
    fields = ['data_pub','enunciado']
    # fieldsets = [(None, ) , (),]
    inlines = [AlternativaInline]
    list_display = ['enunciado', 'id', 'data_pub', 'publicada_recentemente']
    list_filter = ['data_pub']


# Register your models here.
admin.site.register(Pergunta, PerguntaAdmin)
#admin.site.register(Alternativa)