import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Pergunta

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
