from funcoes_validacao_dados import *
from funcoes_interface import *


def criacao_arquivo(nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        titulo = ['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF',  'Data de nascimento', 'Idade']
        for item in titulo:
            if item == titulo[-1]:
                arquivo.write(f'{item}')
            else:
                arquivo.write(f'{item},')
        arquivo.write('\n')
        # Cadastrando um usuário teste - outra forma já colocando a vírgula na lista
        usuario_teste = ['Gabriela,', 'F,', 'gabi@gmail.com,', '(41) 99999-9999,', '111.111.111-22,', '20/12/1994,', '27']
        for dado in usuario_teste:
            arquivo.write(f'{dado}')
        arquivo.write('\n')


def escrita_arquivo(nome_arquivo, usuario):
    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo_escrita:
        for dado in usuario:
            for k, v in dado.items():
                if k == 'idade':
                    arquivo_escrita.write(f'{str(v)}')
                else:
                    arquivo_escrita.write(f'{str(v)},')
            arquivo_escrita.write('\n')


def leitura_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_leitura:
        cadastro = []
        for linha in arquivo_leitura.readlines():
            dado = linha.split(',')
            cadastro.append(dado)
    return cadastro[1:]  # para não retornar o título junto, apenas os usuários


def cadastrar_usuario(nome_arquivo, dados_usuario):
    try:
        dados_usuario['idade'] = calcula_idade(dados_usuario['data_de_nascimento'])
        usuario = [dados_usuario]
        escrita_arquivo(nome_arquivo, usuario)
    except:
        txt = f'Ocorreu algum erro no cadastramento do usuário.'
        print(colorir(txt, cor='vermelha'))
    else:
        txt = f'Cadastro do usuário {dados_usuario["nome"]} realizado com sucesso!'
        print(colorir(txt, cor='verde'))

        print(colorir('Registro do usuário cadastrado:', cor='azul'), end=' ')
        for dado in usuario:
            for k, v in dado.items():
                print(f'{v} - ', end='')
        print()


def buscar_usuario(nome_arquivo, nome):
    cadastro = leitura_arquivo(nome_arquivo)
    for id, usuario in enumerate(cadastro):
        if usuario[0] == nome:
            return cadastro, id, usuario
    return None, None, None


def remover_usuario(nome_arquivo, nome):
    cadastro, id, usuario = buscar_usuario(nome_arquivo, nome)
    if usuario is None:
        txt = f'Não há nenhum usuário no cadastro com o nome {nome}.'
        print(colorir(txt, cor='vermelha'))
    else:
        txt = f'Remoção do usuário {nome} do cadastro realizada com sucesso!'
        print(colorir(txt, cor='verde'))

        print(colorir('Registro do usuário deletado:', cor='azul'), end=' ')
        for lista_dado_usuario in cadastro:
            if lista_dado_usuario == usuario:
                for dado in lista_dado_usuario:
                    dado = dado.rstrip('\n')
                    print(f'{dado} - ', end='')
                print()

        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_leitura:
            linhas = arquivo_leitura.readlines()
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_escrita:
                i = 0
                for linha in linhas:
                    if i != id+1:  # id+1 pois os id's dos usuários começam em 0, mas na linha 1
                        arquivo_escrita.write(f'{linha}')
                    i += 1


def atualizar_usuario(nome_arquivo, nome_original, cadastro, id, usuario, dado_usuario_atualizado, opcao):
    print(colorir('Registro anterior do usuário:', cor='azul'), end=' ')
    for lista_dado_usuario in cadastro:
        if lista_dado_usuario == usuario:
            for dado in lista_dado_usuario:
                dado = dado.rstrip('\n')
                print(f'{dado} - ', end='')
    try:
        for lista_dado_usuario in cadastro:
            if lista_dado_usuario == usuario:
                c = 0
                for dado in lista_dado_usuario:
                    if opcao - 1 == c:
                        lista_dado_usuario[c] = dado_usuario_atualizado
                        if opcao == 6:
                            lista_dado_usuario[c+1] = f'{calcula_idade(dado_usuario_atualizado)}\n'
                    c += 1
                break
    except:
        txt = f'Ocorreu algum erro na atualização do usuário.'
        print(colorir(txt, cor='vermelha'))
    else:
        print(colorir('\nRegistro do usuário após atualização:', cor='azul'), end=' ')
        for lista_dado_usuario in cadastro:
            if lista_dado_usuario == usuario:
                for dado in lista_dado_usuario:
                    dado = dado.rstrip('\n')
                    print(f'{dado} - ', end='')

        txt = f'\nAtualização do usuário {nome_original} realizada com sucesso!'
        print(colorir(txt, cor='verde'))

        titulo = ['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF', 'Data de nascimento', 'Idade\n']
        cadastro.insert(0, titulo)

        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for usuario in cadastro:
                for dado in usuario:
                    if dado == usuario[-1]:
                        arquivo.write(f'{dado}')
                    else:
                        arquivo.write(f'{dado},')

# ARRUMAR ESTATÍSTICAS COM AS DEMAIS OPÇÕES DE GÊNERO ADICIONADAS
def estatisticas(nome_arquivo):
    cont_tot = -1
    cont_f = cont_m = cont_18 = cont_35 = cont_65 = cont_mais_65 = 0

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        lista = arquivo.readlines()
        for i in lista:
            try:
                cont_tot += 1
                lista_item = i.split(',')
                if lista_item[1] == 'F':
                    cont_f += 1
                if lista_item[1] == 'M':
                    cont_m += 1
                if int(lista_item[-1]) < 18:
                    cont_18 += 1
                elif int(lista_item[-1]) < 35:
                    cont_35 += 1
                elif int(lista_item[-1]) < 65:
                    cont_65 += 1
                else:
                    cont_mais_65 += 1
            except:
                pass
    print(colorir('--> ESTATÍSTICAS DO SISTEMA', cor='lilas'), end='')
    print(f'''
    A quantidade de usuários cadastrados é {cont_tot}.
    A quantidade de usuários cadastrados do gênero feminino é {cont_f}.
    A quantidade de usuários cadastrados do gênero masculino é {cont_m}.
    A quantidade de usuários cadastrados do gênero outro é {cont_tot - cont_f - cont_m}.
    A quantidade de usuários cadastrados menores de 18 anos é {cont_18}.
    A quantidade de usuários cadastrados com idade entre 18 e 35 anos é {cont_35}.
    A quantidade de usuários cadastrados com idade entre 35 e 65 anos é {cont_65}.
    A quantidade de usuários cadastrados maiores de 65 anos é {cont_mais_65}.''')
