from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from receitas.models import Receita
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):

    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina
    }

    return render(request, 'receitas/index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    
    receita_a_exibir = {
        'receita' : receita
    }
    
    return render(request,'receitas/receita.html', receita_a_exibir)


def criar_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, 
                                        ingredientes=ingredientes, modo_preparo=modo_preparo, 
                                        tempo_preparo=tempo_preparo, rendimento=rendimento, 
                                        categoria=categoria, foto_receita=foto_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/criar_receita.html')


def deletar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


def editar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_para_editar = {'receita':receita}
    return render(request, 'receitas/editar_receita.html', receita_para_editar)


def atualizar_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        receita_atualizacao = Receita.objects.get(pk=receita_id)
        receita_atualizacao.nome_receita = request.POST['nome_receita']
        receita_atualizacao.ingredientes = request.POST['ingredientes']
        receita_atualizacao.modo_preparo = request.POST['modo_preparo']
        receita_atualizacao.tempo_preparo = request.POST['tempo_preparo']
        receita_atualizacao.rendimento = request.POST['rendimento']
        receita_atualizacao.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            receita_atualizacao.foto_receita = request.FILES['foto_receita']
        receita_atualizacao.save()
        return redirect('dashboard')