from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Evento
from django.utils import timezone


class IndexView(View):
    def get(self, request, *args, **kwargs):
        #Se o evento já tiver sido encerrado, ele não aparece na lista
        lista_eventos = Evento.objects.filter(data_fim__gte = timezone.now())
        contexto = { 'lista_eventos' : lista_eventos}
        return render(request, 'caridade/index.html', contexto)


class DetalhesView(View):
    def get(self, request, *args, **kwargs):
        evento = get_object_or_404(Evento, pk=kwargs['pk'])
        contexto = {'evento': evento}
        return render(request, 'caridade/detalhes.html', contexto)