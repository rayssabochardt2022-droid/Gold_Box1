from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Produto
from django.shortcuts import render, redirect, get_object_or_404


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


def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

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

        categorias_validas = dict(Produto.CATEGORIAS)

        if not all([nome, categoria, marca, preco, estoque]):
            erro = 'Preencha todos os campos obrigatórios.'
        elif categoria not in categorias_validas:
            erro = 'Selecione uma categoria válida.'
        else:
            try:
                preco_valor = float(preco.replace(',', '.'))
                estoque_valor = int(estoque)

                if preco_valor <= 0 or estoque_valor < 0:
                    raise ValueError

                produto.nome = nome
                produto.categoria = categoria
                produto.marca = marca
                produto.preco = preco_valor
                produto.estoque = estoque_valor
                produto.descricao = descricao

                if imagem:
                    produto.imagem = imagem

                produto.save()

                messages.success(
                    request, 'Produto atualizado com sucesso!'
                )
                return redirect('produtos')

            except (ValueError, TypeError):
                erro = 'Informe um preço válido e um estoque inteiro não negativo.'

        return render(request, 'editar_produto.html', {
            'produto': produto,
            'categorias': Produto.CATEGORIAS,
            'dados': dados,
            'erro': erro,
        })

    return render(request, 'editar_produto.html', {
        'produto': produto,
        'categorias': Produto.CATEGORIAS,
    })
