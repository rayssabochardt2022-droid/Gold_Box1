
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dica
from .forms import DicaForm


def lista_dicas(request):
    dicas = Dica.objects.all()
    return render(request, 'dicas/lista.html', {'dicas': dicas})


def cadastrar_dica(request):
    if request.method == 'POST':
        form = DicaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_dicas')
    else:
        form = DicaForm()

    return render(request, 'dicas/cadastrar.html', {'form': form})


def editar_dica(request, pk):
    dica = get_object_or_404(Dica, pk=pk)

    if request.method == 'POST':
        form = DicaForm(request.POST, instance=dica)

        if form.is_valid():
            form.save()
            return redirect('lista_dicas')
    else:
        form = DicaForm(instance=dica)

    return render(request, 'dicas/editar.html', {
        'dica': dica,
        'form': form
    })


def excluir_dica(request, pk):
    dica = get_object_or_404(Dica, pk=pk)

    if request.method == 'POST':
        dica.delete()
        return redirect('lista_dicas')

    return render(request, 'dicas/excluir.html', {'dica': dica})
