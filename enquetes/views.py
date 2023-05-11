from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Pergunta


# Create your views here.
def index(request):
    lista_perguntas = Pergunta.objects.all()
    template = loader.get_template('enquetes/index.html')
    context = {'lista_perguntas': lista_perguntas, }
    return HttpResponse(template.render(context, request))


def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, 'enquetes/detalhes.html', {'pergunta':pergunta})


def votacao(request, pergunta_id):
    resposta = "VOTAÇÃO da Enquete de número %s"
    return HttpResponse(resposta % pergunta_id)


def resultado(request, pergunta_id):
    resposta = "RESULTADOS da Enquete de número %s"
    return HttpResponse(resposta % pergunta_id)