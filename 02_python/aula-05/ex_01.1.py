from pprint import pprint


def titulo(txt):
    print('=' * 50)
    print('{:^50}'.format(txt))
    print('=' * 50)


class InputError(Exception):
    pass


def cadastro_contatos(agenda, nome, tel, email):
    contato = {
        'nome': nome,
        'tel': tel,
        'email': email
    }
    if nome == '' or tel == '' or email == '':
        raise NameError('Faltam informações.')
    if len(tel) != 3:  # considerado 3 algarismos para facilitar
        raise ValueError('Formato de telefone incorreto.')
    if '@' not in email:
        raise InputError('E-mail inválido.')
    else:
        agenda['contatos'].append(contato)
    return agenda


def buscar_contato(agenda, nome):
    for indice, contato in enumerate(agenda['contatos']):
        if nome == contato['nome']:
            return indice, contato
    return None, None


def remover_contato(agenda, nome):
    indice, contato = buscar_contato(agenda, nome)
    if contato:
        del agenda['contatos'][indice]
        return agenda
    else:
        print('Não há nenhum contato na agenda com esse nome.')
        return agenda


agenda = {
    'contatos': []
}

agenda = cadastro_contatos(agenda, 'Gabi', '123', 'gabi@gmail.com')
agenda = cadastro_contatos(agenda, 'Jhony', '456', 'jhony@gmail.com')
agenda = cadastro_contatos(agenda, 'Ana', '789', 'ana@gmail.com')

titulo('AGENDA')

while True:
    print('''
    MENU
    [1] Exibir agenda 
    [2] Cadastrar contato
    [3] Buscar contato
    [4] Remover contato
    [0] Sair
    ''')
    try:
        opcao = int(input('Informe sua opção [1, 2, 3, 4, 0]: '))
    except ValueError as erro:
        print(f'Opção inválida! Erro detectado: {erro.__class__}')
    else:
        while opcao not in [0, 1, 2, 3, 4, 5]:
            print('Opção inválida! Responda novamente:')
            opcao = int(input('Informe sua opção [1, 2, 3, 4, 0]: '))
        if opcao == 1:
            for contato in agenda:
                print('AGENDA:')
                pprint(agenda)
        elif opcao == 2:
            nome = input('Nome: ').strip().capitalize()
            tel = input('Telefone [xxx] : ').strip()  # considerado 3 algarismos para facilitar
            email = input('E-mail: ').strip().lower()
            try:
                agenda = cadastro_contatos(agenda, nome, tel, email)
            except NameError as erro:
                print(f'Erro detectado: {erro}')
            except ValueError as erro:
                print(f'Erro detectado: {erro}')
            except InputError as erro:
                print(f'Erro detectado: {erro}')
            except KeyboardInterrupt:
                break
        elif opcao == 3:
            nome = input('Insira o nome do contato que deseja buscar na agenda: ').capitalize().strip()
            indice, contato = buscar_contato(agenda, nome)
            if contato is None:
                print('Não há nenhum contato na agenda com esse nome.')
            else:
                print(f'DADOS {nome.upper()}:')
                pprint(contato)
        elif opcao == 4:
            nome = input('Insira o nome do contato que deseja remover da agenda: ').capitalize().strip()
            agenda = remover_contato(agenda, nome)
        else:
            break

titulo('PROGRAMA FINALIZADO')
