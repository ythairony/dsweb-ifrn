import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Pergunta(models.Model):
    enunciado = models.CharField(max_length=150)
    data_pub = models.DateTimeField('Data de publicação')
    data_encerramento = models.DateField('Data de encerramento', null=True)
    def __str__(self):
        return self.enunciado
    def publicada_recentemente(self):
        marco_48h_passado = timezone.now() - datetime.timedelta(hours=48)
        agora = timezone.now()
        return (self.data_pub <= agora) and (self.data_pub >= marco_48h_passado)
    def total_de_votos(self):
        total = 0
        for alt in self.alternativa_set.all():
            total += alt.quant_votos
        return total
    def alternativas_ordenadas(self):
        return self.alternativa_set.order_by('-quant_votos')

    publicada_recentemente.admin_order_field = 'data_pub'
    publicada_recentemente.boolean = True
    publicada_recentemente.short_description = 'Recente?'


class Alternativa(models.Model):
    texto = models.CharField(max_length=80)
    quant_votos = models.IntegerField('Quantidade de votos', default=0)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    def __str__(self):
        return self.texto
    def porcentagem(self):
        return (self.quant_votos / self.pergunta.total_de_votos()) * 100