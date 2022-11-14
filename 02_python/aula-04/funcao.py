"""
### Função (function) ###

definição: sequencia nomeada de instruções que encapsula um trecho
de código, podendo ser chamada sempre que necessária pelo seu nome.

aplicações:
- dry (don't repeat yourself)
- apoia automação
- apoia na organização e separação lógica
- apoia na manutenção do código

"""

# definindo uma função

# def nome_da_funcao(parametros):
#     // bloco de código
#     return valor(es)

# função sem argumentos e sem retorno

def print_ola_mundo():
    print('Olá, mundo!')
print_ola_mundo()  # chamando a função

# função com argumentos e sem retorno

def print_ola(nome):
    print(f'Olá, {nome}!')
print_ola('Gabi')  # chamando a função

# função com argumentos posicionais e um retorno

def soma_pos(a, b):
    return a + b
print('5 + 3 =', soma_pos(5, 3))  # chamando a função

# função com argumentos posicionais e um multiplos retornos

def soma_mult(a, b):
    resultado = a + b
    return a, b, resultado
# print(f'a = {a} e b = {b}')

# função com argumentos nomeados e com retorno




# função com argumentos posicionais, nomeados e com retorno



# dicionário como argumentos nomeados

# Fuçando aki, assim tbm dá: print("Opção 2 : " , media_simples(*media_param.values()) )
# No caso, * desempacota a lista


# criando uma função que calcula média a partir de uma lista
# inputs = lista com inteiros ou floats

lista = [2, 5, 3, 6]

def media_lista(lista):
    return sum(lista) / len(lista)

print('Média:', media_lista(lista))

# criando uma função que calcula a área de um retangulo

import math


# criando uma função que calcula a área de um triangulo

def area_triang(base, altura):
    return base * altura / 2

print('Área triângulo:', area_triang(5, 6))


# criando um modulo para funções geometricas
