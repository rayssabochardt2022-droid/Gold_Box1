from django.db import models


class Produto(models.Model):
    CATEGORIAS = [
        ('whey', 'Whey Protein'),
        ('creatina', 'Creatina'),
        ('pre_treino', 'Pré-treino'),
        ('glutamina', 'Glutamina'),
        ('hipercalorico', 'Hipercalórico'),
        ('termogenico', 'Termogênico'),
        ('outros', 'Outros'),
    ]

    nome = models.CharField(max_length=150)
    categoria = models.CharField(max_length=30, choices=CATEGORIAS)
    marca = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(
        upload_to='produtos/',
        blank=True,
        null=True
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
