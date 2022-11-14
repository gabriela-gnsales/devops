"""
Exercício:

1. Criar uma função de cadastro de contatos na agenda (dicionário)
2. Dicionário com uma lista de contatos contendo: nome, telefone e email
3. Cadastrar 3 contatos na agenda utilizando a função

Bônus:
    1. Criar função que busca a retorna um contato a partir do nome
    2. Criar função de deleta um contato a partir do nome
    3. Criar função de atualiza os dados de contato a partir do nome
"""
print('{:*^40}'.format(' EXERCÍCIO '))

from pprint import pprint

agenda = {
    'contatos': []
}

def titulo(txt):
    print('-' * 50)
    print('{:^50}'.format(txt))
    print('-' * 50)

def cadastro_contatos(agenda, dados_contato):
    agenda['contatos'].append(dados_contato)
    return agenda

def buscar_contato(agenda, nome):
    for indice, contato in enumerate(agenda['contatos']):
        if nome == contato['nome']:
            return indice, contato
    return None, None


contato1 = {
    'nome': 'gabi',
    'tel': '123',
    'email': 'gabi@gmail.com'
}

contato2 = {
    'nome': 'jhony',
    'tel': '456',
    'email': 'jhony@gmail.com'
}

contato3 = {
    'nome': 'ana',
    'tel': '789',
    'email': 'ana@gmail.com'
}

titulo('CADASTRO CONTATO')
agenda = cadastro_contatos(agenda, contato1)
agenda = cadastro_contatos(agenda, contato2)
agenda = cadastro_contatos(agenda, contato3)
pprint(agenda)

titulo('BUSCAR CONTATO')
nome = input('Insira o nome do contato que deseja buscar na agenda: ').lower().strip()
contato = buscar_contato(agenda, nome)
# if contato is None:
#     print('Não há nenhum contato na agenda com esse nome.')
pprint(contato)

