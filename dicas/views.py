from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dica
from .forms import DicaForm

def usuario_superuser(user):
    return user.is_authenticated and user.is_superuser

def lista_dicas(request):
    dicas = Dica.objects.all()
    return render(request, 'dicas/lista.html', {'dicas': dicas})

@login_required(login_url='login')
@user_passes_test(usuario_superuser)
def cadastrar_dica(request):
    if request.method == 'POST':
        form = DicaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_dicas')
    else:
        form = DicaForm()

    return render(request, 'dicas/cadastrar.html', {'form': form})

@login_required(login_url='login')
@user_passes_test(usuario_superuser)
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

@login_required(login_url='login')
@user_passes_test(usuario_superuser)
def excluir_dica(request, pk):
    dica = get_object_or_404(Dica, pk=pk)

    if request.method == 'POST':
        dica.delete()
        return redirect('lista_dicas')

    return render(request, 'dicas/excluir.html', {'dica': dica})
