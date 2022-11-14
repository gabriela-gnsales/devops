"""
Exercício:

1. Crie uma agenda utilizando dicionário, a agenda deve ter uma lista de 3 contatos.
2. Os contatos, além do nome, devem possuir telefone e email
3. Verifique se há algum contato com o nome 'marcos'
4. altere o telefone do primeiro contato
5. calcule quantos contatos possuem na lista
"""

print('{:*^40}'.format(' EXERCÍCIO '))

agenda = {
    'contato1': {
        'nome': 'Gabriela',
        'telefone': 999999999,
        'email': 'gabi@gmail.com'
    },
    'contato2': {
        'nome': 'Marcos',
        'telefone': 222222222,
        'email': 'marcos@gmail.com'
    },
    'contato3': {
        'nome': 'Paulo',
        'telefone': 333333333,
        'email': 'paulo@gmail.com'
    },
    # 'contato4': {
    #     'nome': 'Ana',
    #     'telefone': 444444444,
    #     'email': 'ana@gmail.com'
    # }
}

print(agenda)

cont = 0

# for i, j in agenda.items():
#     if 'Marcos' in agenda[i]['nome']:
#         cont += 1

for contato in agenda:
    if 'marcos' in agenda[contato]['nome'].lower().strip():
        cont += 1

if cont > 0:
    print(f'Há {cont} contato(s) com o nome "Marcos".')
else:
    print('Não há nenhum contato chamado "Marcos".')

agenda['contato1']['telefone'] = 111111111
print(agenda)

print('Quantidade de contatos na agenda:', len(agenda))
