def colorir(msg, estilo='negrito', cor='branca'):
    cod_estilo = {
        'nenhum': 0,
        'negrito': 1,
        'underline': 4,
        'inverso': 7
    }
    cod_texto = {
        'branca': 30,
        'vermelha': 31,
        'verde': 32,
        'amarela': 33,
        'azul': 34,
        'lilas': 35,
        'ciano': 36,
        'cinza': 37
    }
    msg = f'\033[{cod_estilo[estilo]};{cod_texto[cor]}m{msg}\033[m'
    return msg


def linha(cor_l, simbolo='-', tamanho=50):
    print(colorir(f'{simbolo * tamanho}', cor=cor_l))


def titulo1(texto, cor_t1, cor_l='branca', simbolo='-', tamanho=50):
    linha(cor_l, simbolo, tamanho)
    txt = f'{texto:^{tamanho}}'
    print(colorir(txt, cor=cor_t1))
    linha(cor_l, simbolo, tamanho)


def titulo2(texto, cor_t2, simbolo='-', tamanho=50):
    txt = f'{texto:{simbolo}^{tamanho}}'
    print(colorir(txt, cor=cor_t2))


def titulo_arquivo(cor_t_a):
    titulo = ['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF', 'Data de nascimento', 'Idade']
    for item in titulo:
        txt = f'{item:^20}'
        print(colorir(txt, cor=cor_t_a), end='')
    print()


def leia_inteiro(msg, lista_range):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError) as erro:
            txt = f'Opção inválida! Erro detectado: {erro.__class__}.'
            print(colorir(txt, cor='vermelha'))
        else:
            if n in lista_range:
                return n
                break
            txt = f'Opção inválida! Responda um número entre {lista_range[0]} e {lista_range[-1]}.'
            print(colorir(txt, cor='vermelha'))


def menu(lista, simbolo='-', tamanho=50, cor='amarela'):
    titulo2(' MENU ', cor, simbolo, tamanho)
    c = 1
    for item in lista:
        txt = f'[{c}] {item}'
        print(colorir(txt, cor=cor))
        c += 1
    linha(cor, simbolo, tamanho)
    opcao = leia_inteiro('Informe sua opção: ', range(1, c))
    return opcao
