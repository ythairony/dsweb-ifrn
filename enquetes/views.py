from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Pergunta, Alternativa


# Create your views here.
def index(request):
    lista_perguntas = Pergunta.objects.all()
    context = {'lista_perguntas': lista_perguntas, }
    return render(request, 'enquetes/index.html', context)


def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, 'enquetes/detalhes.html', {'pergunta':pergunta})


def votacao(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        id_alternativa = request.POST['escolha']
        alt_selecionada = pergunta.alternativa_set.get(pk=id_alternativa)
    except (KeyError, Alternativa.DoesNoteExist):
        contexto = {
            'pergunta':pergunta,
            'error': 'Você precisa selecionar uma alternativa'
        }
        return render(request, 'enquetes/detalhes.html', contexto)
    else:
        alt_selecionada.quant_votos += 1
        alt_selecionada.save()
        return HttpResponseRedirect(reverse('enquetes:resultado', args=(pergunta.id,)))

def resultado(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, 'enquetes/resultado.html', {'pergunta':pergunta})