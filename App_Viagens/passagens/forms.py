from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.models import Passagem, ClasseViagem, Pessoa
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *

class PassagemForms(forms.ModelForm):
    
    data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today)
    
    class Meta: 
        model = Passagem
        fields = '__all__'
        labels = {'data_ida':'Data de Ida', 'data_volta':'Data de Volta', 
                'informacoes':'Informações', 'classe_viagem':'Classe do Vôo'}
        widgets = {
            'data_ida':DatePicker(),
            'data_volta':DatePicker() 
        }
    
    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_erros = {}
        campo_tem_numero(origem, 'origem', lista_erros)
        campo_tem_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        comparacao_datas(data_ida, data_volta, lista_erros)
        compra_retrograda(data_ida, data_pesquisa, lista_erros)
        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data


class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']

