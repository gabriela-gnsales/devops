import crud
from pprint import pprint

agenda = {
    'contatos': [
        # {
        #     'nome': 'gabi',
        #     'tel': '123',
        #     'email': 'gabi@gmail.com'
        # }
    ]
}

novo_contato = {
    'nome': 'gabi',
    'tel': '123',
    'email': 'gabi@gmail.com'
}

agenda = crud.criar_contato(agenda, novo_contato)
pprint(agenda)

print('\n2. Buscar contato:')
buscar_nome = 'gabi'
contato = crud.buscar_contato(agenda, buscar_nome)
pprint(contato)

print('\n3. Remover contato:')
remover_nome = 'gabi'
agenda = crud.remover_contato(agenda, remover_nome)
pprint(agenda)

print('\n3. Atualizar contato:')
atualizar_nome = 'jhony'
atualizar_dados = {
    'tel': '9999999',
    'email': 'jhony@gmail.com'
}
agenda = crud.atualizar_contato(agenda, atualizar_nome, atualizar_dados)
pprint(agenda)
