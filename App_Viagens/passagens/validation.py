def origem_destino_iguais(origem, destino, lista_erros):
    if origem == destino:
        lista_erros['destino'] = "Origem e Destino não podem ser iguais"

def campo_tem_numero(valor_campo, nome_campo, lista_erros):
        if any(char.isdigit() for char in valor_campo):
            lista_erros[nome_campo] = "Este campo não aceita números"

def comparacao_datas(data_ida, data_volta, lista_erros):
    if data_ida > data_volta:
        lista_erros['data_volta'] = "A data de ida não pode ser posterior à data de volta"

def compra_retrograda(data_ida, data_pesquisa, lista_erros):
    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = "A data de ida não pode ser anterior à data de hoje"

