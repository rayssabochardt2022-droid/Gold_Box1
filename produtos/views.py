from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Produto


def produtos(request):
    lista_produtos = Produto.objects.all()

    return render(request, 'produtos.html', {
        'produtos': lista_produtos
    })


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        categoria = request.POST.get('categoria', '')
        marca = request.POST.get('marca', '').strip()
        preco = request.POST.get('preco', '').strip()
        estoque = request.POST.get('estoque', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        imagem = request.FILES.get('imagem')

        dados = {
            'nome': nome,
            'categoria': categoria,
            'marca': marca,
            'preco': preco,
            'estoque': estoque,
            'descricao': descricao,
        }

        if not all([nome, categoria, marca, preco, estoque]):
            return render(request, 'cadastro.html', {
                'erro': 'Preencha todos os campos obrigatórios.',
                'dados': dados,
            })

        categorias_validas = dict(Produto.CATEGORIAS)

        if categoria not in categorias_validas:
            return render(request, 'cadastro.html', {
                'erro': 'Selecione uma categoria válida.',
                'dados': dados,
            })

        try:
            preco_valor = preco.replace(',', '.')
            preco_valor = float(preco_valor)

            if preco_valor <= 0:
                raise ValueError

            estoque_valor = int(estoque)

            if estoque_valor < 0:
                raise ValueError

            Produto.objects.create(
                nome=nome,
                categoria=categoria,
                marca=marca,
                preco=preco_valor,
                estoque=estoque_valor,
                descricao=descricao,
                imagem=imagem,
            )

        except (ValueError, TypeError):
            return render(request, 'cadastro.html', {
                'erro': 'Informe um preço válido e um estoque inteiro não negativo.',
                'dados': dados,
            })

        messages.success(request, 'Produto cadastrado com sucesso!')
        return redirect('produtos')

    return render(request, 'cadastro.html')
