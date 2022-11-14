from funcoes_interface import *
from datetime import date
import re


def valida_genero():
    print('''Gênero 
    [1] Feminino
    [2] Masculino
    [3] Não binário
    [4] Outro gênero
    [5] Prefiro não responder''')
    genero = leia_inteiro('Informe sua opção: ', range(1, 6))
    if genero == 1:
        return 'Feminino'
    elif genero == 2:
        return 'Masculino'
    elif genero == 3:
        return 'Não binário'
    elif genero == 4:
        return 'Outro gênero'
    else:
        return 'Prefiro não responder'
    # while True:
    #     genero = input('Gênero [M/F/Outro]: ').strip().upper()[0]
    #     if genero in 'MFO':
    #         break
    #     txt = 'Erro! Responda apenas M, F ou Outro.'
    #     print(colorir(txt, cor='vermelha'))
    # return genero


def valida_email():
    while True:
        email = input('E-mail: ').strip()
        padrao = re.search(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', email)
        if padrao:
            break
        else:
            txt = 'Erro! Insira um e-mail válido.'
            print(colorir(txt, cor='vermelha'))
    return email


def valida_telefone():
    while True:
        telefone = input('Telefone [(DDD) XXXXX-XXXX]: ').strip()
        padrao = re.search(r'^\([0-9]{2}\) [0-9]{4,5}-[0-9]{4}$', telefone)
        # padrao = re.search(r'^\([0-9]{2}\) (?:9[0-9]{1}|[1-5]{1})[0-9]{3}-[0-9]{4}$', telefone)
        if padrao:
            break
        else:
            txt = 'Erro! Insira o telefone no formato solicitado.'
            print(colorir(txt, cor='vermelha'))
    return telefone


def valida_cpf():
    """
    Efetua a validação do CPF, tanto formatação quando dígito verificadores.

    FONTE: https://pt.stackoverflow.com/questions/64608/como-validar-e-calcular-o-d%C3%ADgito-de-controle-de-um-cpf#:~:text=A%20valida%C3%A7%C3%A3o%20do%20CPF%20%C3%A9,fornecida%2C%20o%20CPF%20%C3%A9%20valido.

        Parâmetros:
            cpf (str): CPF a ser validado

        Retorno:
            bool:
                - Falso, quando o CPF não possuir o formato 999.999.999-99;
                - Falso, quando o CPF não possuir 11 caracteres numéricos;
                - Falso, quando os dígitos verificadores forem inválidos;
                - Verdadeiro, caso contrário.

        Exemplos:

            >>> validate('529.982.247-25')
        True
            >>> validate('52998224725')
        False
            >>> validate('111.111.111-11')
        False
    """
    while True:
        cpf = input('CPF [XXX.XXX.XXX-XX]: ').strip()
        txt = 'Erro! Insira um CPF válido.'
        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]
        sum_of_products_1 = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit_1 = (sum_of_products_1 * 10 % 11) % 10
        sum_of_products_2 = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit_2 = (sum_of_products_2 * 10 % 11) % 10
        # Verifica a formatação do CPF
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            print(colorir(txt, cor='vermelha'))
        # Verifica se o CPF possui 11 números ou se todos são iguais
        elif len(numbers) != 11 or len(set(numbers)) == 1:
            print(colorir(txt, cor='vermelha'))
        # Validação do primeiro dígito verificador
        elif numbers[9] != expected_digit_1:
            print(colorir(txt, cor='vermelha'))
        # Validação do segundo dígito verificador
        elif numbers[10] != expected_digit_2:
            print(colorir(txt, cor='vermelha'))
        else:
            break
    return cpf


def valida_data(data):  # função usada nas funções 'valida_data_de_nascimento' e 'calcula_idade'
    data_processada = data.split('/')
    dia = int(data_processada[0])
    mes = int(data_processada[1])
    ano = int(data_processada[2])
    return dia, mes, ano


def valida_data_de_nascimento():
    while True:
        data_de_nascimento = input('Data de nascimento [dd/mm/aaaa]: ').strip()
        try:
            dia, mes, ano = valida_data(data_de_nascimento)
        except Exception as erro:
            txt = f'Erro detectado: {erro.__class__}. Insira a data no formato solicitado.'
            print(colorir(txt, cor='vermelha'))
        else:
            if date(ano, mes, dia) > date.today():
                txt = 'Erro! Insira uma data válida (inferior ao dia de hoje).'
                print(colorir(txt, cor='vermelha'))
            else:
                break
    return data_de_nascimento


def calcula_idade(data_de_nascimento):
    dia, mes, ano = valida_data(data_de_nascimento)
    idade = date.today().year - ano - ((date.today().month, date.today().day) < (mes, dia))
    return idade

