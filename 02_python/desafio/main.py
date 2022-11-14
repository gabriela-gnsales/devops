from funcoes_sistema import *
from funcoes_validacao_dados import *
from os.path import isfile
from time import sleep

arquivo_cadastro = 'cadastro_usuarios.txt'

titulo1('INÍCIO PROGRAMA', 'ciano', 'cinza', '=', 155)

if isfile(arquivo_cadastro) is False:
    criacao_arquivo(arquivo_cadastro)

while True:
    opcao = menu(['Exibir lista de usuários', 'Buscar usuário', 'Cadastrar usuário', 'Remover usuário', 'Atualizar dados usuário', 'Estatísticas do sistema', 'Sair'], simbolo='-', tamanho=30)

    if opcao == 1:
        cadastro = leitura_arquivo(arquivo_cadastro)
        if len(cadastro) == 0:
            txt = f'Não há nenhum usuário cadastrado no sistema.'
            print(colorir(txt, cor='vermelha'))
        else:
            linha('lilas', '-', 140)
            titulo_arquivo('lilas')
            for usuario in cadastro:
                for dado in usuario:
                    # dado = dado.replace('\n', '')
                    dado = dado.rstrip('\n')
                    print(f'{dado:^20}', end='')
                print()
            linha('lilas', '-', 140)

    elif opcao == 2:
        nome = input('Insira o nome do usuário que deseja buscar no cadrasto: ').capitalize().strip()
        cadastro, id, usuario = buscar_usuario(arquivo_cadastro, nome)
        if usuario:
            linha('lilas', '-', 140)
            titulo_arquivo('lilas')
            for dado in usuario:
                dado = dado.rstrip('\n')
                print(f'{dado:^20}', end='')
            print()
            linha('lilas', '-', 140)
        else:
            txt = f'Não há nenhum usuário no cadastro com o nome {nome}.'
            print(colorir(txt, cor='vermelha'))

    elif opcao == 3:
        dados_usuario = dict()
        dados_usuario['nome'] = input('Nome: ').strip().capitalize()
        dados_usuario['genero'] = valida_genero()
        dados_usuario['email'] = valida_email()
        dados_usuario['telefone'] = valida_telefone()
        dados_usuario['cpf'] = valida_cpf()
        dados_usuario['data_de_nascimento'] = valida_data_de_nascimento()
        cadastrar_usuario(arquivo_cadastro, dados_usuario)

    elif opcao == 4:
        nome = input('Insira o nome do usuário que deseja remover do cadastro: ').capitalize().strip()
        remover_usuario(arquivo_cadastro, nome)

    elif opcao == 5:
        nome_original = input('Insira o nome do usuário que deseja atualizar os dados no cadastro: ').capitalize().strip()
        cadastro, id, usuario = buscar_usuario(arquivo_cadastro, nome_original)
        if usuario:
            print('Qual informação deseja atualizar?')
            opcao = menu(['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF', 'Data de nascimento'], simbolo='-', tamanho=30, cor='azul')
            if opcao == 1:
                dado_usuario_atualizado = input('Nome: ').strip().capitalize()
            elif opcao == 2:
                dado_usuario_atualizado = valida_genero()
            elif opcao == 3:
                dado_usuario_atualizado = valida_email()
            elif opcao == 4:
                dado_usuario_atualizado = valida_telefone()
            elif opcao == 5:
                dado_usuario_atualizado = valida_cpf()
            else:
                dado_usuario_atualizado = valida_data_de_nascimento()
            atualizar_usuario(arquivo_cadastro, nome_original, cadastro, id, usuario, dado_usuario_atualizado, opcao)

        else:
            txt = f'Não há nenhum usuário no cadastro com o nome {nome_original}.'
            print(colorir(txt, cor='vermelha'))

    elif opcao == 6:
        estatisticas(arquivo_cadastro)
    else:
        break
    sleep(1)

titulo1('PROGRAMA FINALIZADO', 'ciano', 'cinza', '=', 155)
