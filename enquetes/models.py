import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Pergunta(models.Model):
    enunciado = models.CharField(max_length=150)
    data_pub = models.DateTimeField('Data de publicação')
    def __str__(self):
        return self.enunciado
    def publicada_recentemente(self):
        return self.data_pub >= timezone.now() - datetime.timedelta(hours=48)


class Alternativa(models.Model):
    texto = models.CharField(max_length=80)
    quant_votos = models.IntegerField('Quantidade de votos', default=0)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    def __str__(self):
        return self.texto