

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Publicacao
from .forms import PublicacaoForm


def pode_gerenciar_blog(user):
    return user.is_authenticated and user.is_staff


def post_list(request):
    publicacoes = Publicacao.objects.filter(
        publicado=True
    ).select_related('autor')

    return render(
        request,
        'blog/post_list.html',
        {'publicacoes': publicacoes}
    )


def post_detail(request, pk):
    publicacao = get_object_or_404(
        Publicacao,
        pk=pk,
        publicado=True
    )

    return render(
        request,
        'blog/post_detail.html',
        {'publicacao': publicacao}
    )


@login_required
@user_passes_test(pode_gerenciar_blog)
def post_create(request):
    if request.method == 'POST':
        form = PublicacaoForm(request.POST)

        if form.is_valid():
            publicacao = form.save(commit=False)
            publicacao.autor = request.user
            publicacao.save()
            return redirect('blog:post_list')
    else:
        form = PublicacaoForm()

    return render(request, 'blog/post_form.html', {
        'form': form,
        'titulo_pagina': 'Nova publicação',
    })


@login_required
@user_passes_test(pode_gerenciar_blog)
def post_update(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)

    if request.method == 'POST':
        form = PublicacaoForm(
            request.POST,
            instance=publicacao
        )

        if form.is_valid():
            form.save()
            return redirect(
                'blog:post_detail',
                pk=publicacao.pk
            )
    else:
        form = PublicacaoForm(instance=publicacao)

    return render(request, 'blog/post_form.html', {
        'form': form,
        'titulo_pagina': 'Editar publicação',
    })


@login_required
@user_passes_test(pode_gerenciar_blog)
def post_delete(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)

    if request.method == 'POST':
        publicacao.delete()
        return redirect('blog:post_list')

    return render(request, 'blog/post_confirm_delete.html', {
        'publicacao': publicacao,
    })