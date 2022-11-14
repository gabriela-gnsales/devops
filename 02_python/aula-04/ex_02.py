from pprint import pprint


def titulo(txt):
    print('=' * 50)
    print('{:^50}'.format(txt))
    print('=' * 50)


def cadastro_contatos(agenda, dados_contato):
    agenda['contatos'].append(dados_contato)
    return agenda


def buscar_contato(agenda, nome):
    for indice, contato in enumerate(agenda['contatos']):
        if nome == contato['nome']:
            return indice, contato
    return None, None


agenda = {
    'contatos': []
}
contato1 = {
    'nome': 'Gabi',
    'tel': '123',
    'email': 'gabi@gmail.com'
}
contato2 = {
    'nome': 'Jhony',
    'tel': '456',
    'email': 'jhony@gmail.com'
}
contato3 = {
    'nome': 'Ana',
    'tel': '789',
    'email': 'ana@gmail.com'
}

agenda = cadastro_contatos(agenda, contato1)
agenda = cadastro_contatos(agenda, contato2)
agenda = cadastro_contatos(agenda, contato3)

titulo('AGENDA')

while True:
    print('''
    MENU
    [1] Exibir agenda 
    [2] Cadastrar contato
    [3] Buscar contato
    [0] Sair
    ''')
    opcao = int(input('Informe sua opção (1, 2, 3, 0): '))
    while opcao not in [0, 1, 2, 3]:
        print('Opção inválida. Responda novamente:')
        opcao = int(input('Informe sua opção (1, 2, 3, 0): '))
    if opcao == 1:
        for contato in agenda:
            print('AGENDA:')
            pprint(agenda)
    elif opcao == 2:
        contato = {
            'nome': input('Nome: ').strip().capitalize(),
            'tel': input('Telefone: ').strip(),
            'email': input('E-mail: ').strip().lower()}
        agenda = cadastro_contatos(agenda, contato)
    elif opcao == 3:
        nome = input('Insira o nome do contato que deseja buscar na agenda: ').capitalize().strip()
        contato = buscar_contato(agenda, nome)
        print(f'DADOS {nome.upper()}:')
        pprint(contato)
    else:
        break

titulo('PROGRAMA FINALIZADO')
