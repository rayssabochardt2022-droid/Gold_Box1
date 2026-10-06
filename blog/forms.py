

from django import forms
from .models import Publicacao


class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = [
            'titulo',
            'resumo',
            'conteudo',
            'publicado',
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título da publicação',
            }),
            'resumo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Resumo da publicação',
            }),
            'conteudo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Escreva o conteúdo aqui',
            }),
            'publicado': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }