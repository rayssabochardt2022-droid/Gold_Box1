from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Dica


def lista_dicas(request):
    dicas = Dica.objects.all()
    return render(request, 'dicas/lista.html', {'dicas': dicas})


def cadastrar_dica(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        categoria = request.POST.get('categoria')

        Dica.objects.create(
            titulo=titulo,
            conteudo=conteudo,
            categoria=categoria
        )

        return redirect('lista_dicas')

    return render(request, 'dicas/cadastrar.html')