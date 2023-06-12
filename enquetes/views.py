from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.utils import timezone
from django.http import HttpResponseRedirect, Http404
from .models import Pergunta, Alternativa


# Create your views here.
'''
def index(request):
    lista_perguntas = Pergunta.objects.all()
    context = {'lista_perguntas': lista_perguntas, }
    return render(request, 'enquetes/index.html', context)

class IndexView(generic.ListView):
    template_name = 'enquetes/index.html'
    context_object_name = 'lista_perguntas'
    def get_queryset(self):
        return Pergunta.objects.order_by('-data_pub')

'''

class IndexView(View):
    def get(self, request, *args, **kwargs):
        # lista_perguntas = Pergunta.objects.order_by('-data_pub')
        lista_perguntas = Pergunta.objects.filter(
            data_encerramento__gte = timezone.now()
        ).filter(
            data_pub__lte = timezone.now()
        ).order_by('data_pub')
        contexto = {'lista_perguntas': lista_perguntas, }
        return render(request, 'enquetes/index.html', contexto)


class EncerradasView(View):
    def get(self, request, *args, **kwargs):
        # lista_perguntas = Pergunta.objects.order_by('-data_pub')
        lista_perguntas = Pergunta.objects.filter(data_encerramento__lt = timezone.now()).order_by('data_pub')
        contexto = {'lista_perguntas': lista_perguntas, }
        return render(request, 'enquetes/encerradas.html', contexto)

'''
def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, 'enquetes/detalhes.html', {'pergunta':pergunta})


class DetalhesView(generic.DetailView):
    model = Pergunta
    template_name = 'enquetes/detalhes.html'
'''

class DetalhesView(View):
    def get(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk=kwargs['pk'])
        if pergunta.data_pub > timezone.now():
            raise Http404('Nenhuma pergunta com tal identificação.')
        return render(request, 'enquetes/detalhes.html', {'pergunta':pergunta})

'''
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
'''

class VotacaoView(View):
    def post(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk=kwargs['pk'])
        try:
            id_alternativa = request.POST['escolha']
            alt_selecionada = pergunta.alternativa_set.get(pk=id_alternativa)
        except (KeyError, Alternativa.DoesNotExist):
            contexto = {
                'pergunta':pergunta,
                'error': 'Você precisa selecionar uma alternativa'
            }
            return render(request, 'enquetes/detalhes.html', contexto)
        else:
            alt_selecionada.quant_votos += 1
            alt_selecionada.save()
            return HttpResponseRedirect(reverse('enquetes:resultado', args=(pergunta.id,)))

'''
def resultado(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, 'enquetes/resultado.html', {'pergunta':pergunta})


class ResultadoView(generic.DetailView):
    model = Pergunta
    template_name = 'enquetes/resultado.html'
'''


class ResultadoView(View):
    def get(self, request, *args, **kwargs):
        pergunta = get_object_or_404(Pergunta, pk=kwargs['pk'])
        return render(request, 'enquetes/resultado.html', {'pergunta':pergunta})