import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Pergunta


def criar_pergunta(texto, dias):
    """
    Criar uma isntância de pergunta com um dado enunciado e uma data
    """
    data = timezone.now() + datetime.timedelta(days=dias)
    return Pergunta.objects.create(
        enunciado=texto, data_pub=data,
        data_encerramento = timezone.now() + datetime.timedelta(days=30)
    )


class DetalhesViewTest(TestCase):
    def test_com_pergunta_no_futuro(self):
        """
        Ao tentar exibir detalhes de uma pergunta no futuro recebemos um 404
        """
        pergunta = criar_pergunta('Pergunta futura', 5)
        url = reverse('enquetes:detalhes', args=(pergunta.id,))
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, 404)



class IndexViewTest(TestCase):
    def test_pergunta_com_data_futura(self):
        """
        Pergunta com data no futuro não deve ser exibida na Index
        """
        criar_pergunta('Pergunta no futuro', 1)
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertContains(resposta, 'Nenhuma enquete cadastrada')
        self.assertQuerysetEqual(resposta.context['lista_perguntas'], [])

    def test_sem_perguntas_cadastradas(self):
        """
        Não havendo perguntas é exibida uma mensagem correspondente
        """
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Nenhuma enquete cadastrada')
        self.assertQuerysetEqual(resposta.context['lista_perguntas'], [])

    def test_pergunta_com_data_passada(self):
        """
        Pergunta com data no passado são exibidos normalmente
        """
        criar_pergunta('Pergunta no passado', -1)
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Pergunta no passado')
        self.assertQuerysetEqual(
            resposta.context['lista_perguntas'],
            ['<Pergunta: Pergunta no passado>']
        )

    def test_pergunta_com_data_futura_e_passada(self):
        """
        Só deve ser exibida a pergunta com data no passado
        """
        criar_pergunta('Pergunta no passado', -1)
        criar_pergunta('Pergunta no futuro', 1)
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Pergunta no passado')
        self.assertQuerysetEqual(
            resposta.context['lista_perguntas'],
            ['<Pergunta: Pergunta no passado>'])



class PerguntaModelTest(TestCase):
    def test_publicada_recentemente_com_pergunta_no_futuro(self):
        """
        Ao invocar o método com data no futuro a resposta DEVE ser False
        """

        data = timezone.now() + datetime.timedelta(days=30)
        pergunta = Pergunta(data_pub=data)
        self.assertIs(pergunta.publicada_recentemente(), False)


    def test_publicada_recentemente_com_pergunta_alem_das_48hs(self):
        """
        Ao invocar o método com data anterior a 48 horas a resposta DEVE ser False
        """

        data = timezone.now() - datetime.timedelta(days=2, seconds=1)
        pergunta = Pergunta(data_pub=data)
        self.assertIs(pergunta.publicada_recentemente(), False)


    def test_publicada_recentemente_com_pergunta_dentro_das_48hs(self):
        """
        Ao invocar o método com data dentro a 48 horas a resposta DEVE ser True
        """

        data = timezone.now()
        pergunta = Pergunta(data_pub=data)
        self.assertIs(pergunta.publicada_recentemente(), True)


# Create your tests here.
