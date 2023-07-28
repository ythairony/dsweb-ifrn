from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField('Data de início')
    data_fim = models.DateField('Data de encerramento')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class Item(models.Model):
    imagem = models.ImageField(upload_to='imagem_item/', null=True, blank=True)
    descricao = models.CharField(max_length=50)
    valor = models.FloatField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.descricao

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.descricao} reservado por: {self.usuario.username}"


