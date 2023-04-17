from django.shortcuts import render
from receitas.models import Receita

def buscar(request):

    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_buscado = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_buscado)
    
    dados = {
        'receitas' : lista_receitas
    }

    return render(request,'receitas/busca.html', dados)