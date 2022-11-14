"""
1. Use o seu código produzido para o exercício da aula 04, para aplicar os
devidos tratamentos de erros usando o Try e Except da forma que julgar
necessário.
"""

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
    if len(tel) != 3:  # 15 contanto (), espaço e -
        raise ValueError('Formato de telefone incorreto.')  # verificar se é erro de valor mesmo
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
        # agenda['contatos'].pop(indice)
        return agenda
    else:
        print('Não há nenhum contato na agenda com esse nome.')
        return agenda


# def atualizar_contato(agenda, nome, dado, dados_atualizados):
#     indice, contato = buscar_contato(agenda, nome)
#     if contato:
#         if dado == 1:
#
#
#         return agenda
#     else:
#         print('Não há nenhum contato na agenda com esse nome.')
#         return agenda


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
    [5] Atualizar contato
    [0] Sair
    ''')
    try:
        opcao = int(input('Informe sua opção [1, 2, 3, 4, 5, 0]: '))
    except ValueError as erro:
        print(f'Opção inválida! Erro detectado: {erro.__class__}')
    else:
        while opcao not in [0, 1, 2, 3, 4, 5]:
            print('Opção inválida! Responda novamente:')
            opcao = int(input('Informe sua opção [1, 2, 3, 4, 5, 0]: '))
        if opcao == 1:
            for contato in agenda:
                print('AGENDA:')
                pprint(agenda)
        elif opcao == 2:
            nome = input('Nome: ').strip().capitalize()
            tel = input('Telefone [xxx] : ').strip()  # (xx) xxxxx-xxxx
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
        elif opcao == 5:
            nome = input('Insira o nome do contato que deseja atualizar os dados na agenda: ').capitalize().strip()
            try:
                print('''Qual dado deseja atualizar:
                [1] Nome
                [2] Telefone
                [3] E-mail
                ''')
                dado = int(input('Opção: '))
            except ValueError as erro:
                print(f'Opção inválida! Erro detectado: {erro.__class__}')
            else:
                while dado not in [1, 2, 3]:
                    print('Opção inválida! Responda novamente:')
                    dado = int(input('Opção [1, 2 ou 3]: '))
                if dado == 1:
                    nome_atualizado = input('Nome: ').strip().capitalize()
                    dados_atualizados = {
                        'nome': nome_atualizado
                    }
                elif dado == 2:
                    tel_atualizado = input('Telefone [xxx] : ').strip()
                    dados_atualizados = {
                        'tel': tel_atualizado
                    }
                else:
                    email_atualizado = input('E-mail: ').strip().lower()
                    dados_atualizados = {
                        'email': email_atualizado
                    }
                agenda = atualizar_contato(agenda, nome, dados_atualizados)
        else:
            break

titulo('PROGRAMA FINALIZADO')
