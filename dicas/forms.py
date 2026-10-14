
from django import forms
from .models import Dica


class DicaForm(forms.ModelForm):
    class Meta:
        model = Dica
        fields = ['titulo', 'conteudo', 'categoria']

        labels = {
            'titulo': 'Título',
            'conteudo': 'Conteúdo',
            'categoria': 'Categoria',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título da dica'
            }),
            'conteudo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o conteúdo da dica',
                'rows': 5
            }),
            'categoria': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a categoria da dica'
            }),
        }
