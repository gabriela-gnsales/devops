'''
Descrição
Autor: ...
'''

def criar_contato(agenda, dados_contato):
    agenda['contatos'].append(dados_contato)
    return agenda

def buscar_contato(agenda, nome):
    for indice, contato in enumerate(agenda['contatos']):
        if nome == contato['nome']:
            return indice, contato
    return None, None

def remover_contato(agenda, nome):
    indice, contato = buscar_contato(agenda, nome)
    if contato:
        agenda['contatos'].pop(indice)
        return agenda
    else:
        print('Contato não existe.')
        return agenda

def atualizar_contato(agenda, nome, dados_contato):
    indice, contato = buscar_contato(agenda, nome)
    for key, value in dados_contato.items():
        agenda['contatos'][indice][key] = value
    return agenda

