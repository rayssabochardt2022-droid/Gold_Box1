from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
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


def editar_dica(request, pk):
    dica = get_object_or_404(Dica, pk=pk)

    if request.method == 'POST':
        dica.titulo = request.POST.get('titulo')
        dica.conteudo = request.POST.get('conteudo')
        dica.categoria = request.POST.get('categoria')

        dica.save()

        return redirect('lista_dicas')

    return render(request, 'dicas/editar.html', {'dica': dica})