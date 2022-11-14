### ARQUIVOS

# 1. Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e
# gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos

# - O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

# - O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
#
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256

# MODO 1
'''
invalido = ['257.32.4.5\n', '85.345.1.2\n', '9.8.234.5\n', '192.168.0.256']
ip_invalido = []

with open('./lista_IP.txt', 'r') as arquivo_leitura,\
    open('./lista_validos_invalidos.txt', 'w', encoding = 'utf-8') as arquivo_escrita:

    linha = arquivo_leitura.readlines()

    arquivo_escrita.write('[Endereços válidos:]\n')
    for item in linha:
        if item in invalido:
            ip_invalido.append(item)
        else:
            arquivo_escrita.write(item)

    arquivo_escrita.write('[Endereços inválidos:]\n')
    for i in ip_invalido:
        arquivo_escrita.write(i)
'''

# MODO 2 - CORRIGIR

with open('./lista_IP.txt', 'r') as arquivo_leitura,\
    open('./lista_validos_invalidos_2.txt', 'w', encoding='utf-8') as arquivo_escrita:

    linha = arquivo_leitura.readlines()

    arquivo_escrita.write('[Endereços válidos:]\n')
    for item in linha:
        lista = item.split('.')
        for i in lista:
            i = int(i)
            # if i <= 255 and i >= 0:
            if 0 <= i <= 255:
                arquivo_escrita.write(item)

    arquivo_escrita.write('[Endereços inválidos:]\n')
    for item in linha:
        lista = item.split('.')
        for i in lista:
            i = int(i)
            if 0 <= i <= 255:
                arquivo_escrita.write(item)
