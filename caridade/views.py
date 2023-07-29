from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Evento

class IndexView(View):
    def get(self, request, *args, **kwargs):
        lista_eventos = Evento.objects.all()
        contexto = { 'lista_eventos' : lista_eventos}
        return render(request, 'caridade/index.html', contexto)


class DetalhesView(View):
    def get(self, request, *args, **kwargs):
        evento = get_object_or_404(Evento, pk=kwargs['pk'])
        contexto = {'evento': evento}
        return render(request, 'caridade/detalhes.html', contexto)