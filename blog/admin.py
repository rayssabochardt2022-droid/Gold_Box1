
from django.contrib import admin
from .models import Publicacao


@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'autor',
        'data_criacao',
        'publicado',
    )

    search_fields = ('titulo', 'resumo', 'conteudo')
    list_filter = ('publicado', 'data_criacao')

