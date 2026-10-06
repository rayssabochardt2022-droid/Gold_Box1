
from django.db import models
from django.contrib.auth.models import User


class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.CharField(max_length=300)
    conteudo = models.TextField()

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=True)

    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.titulo








