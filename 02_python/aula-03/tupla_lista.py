"""
### Tupla (tuple) ###

definição: é um container que armazena elementos/objetos
de forma sequencial, imutável e iterável.

### Lista (list) ###

definição: é um container que armazena elementos/objetos
de forma sequencial, mutável e iterável.

Diferença de LISTA e TUPLA: uma é MULTÁVEL (lista) e a outra IMUTÁVEL (tupla)
"""

# criando uma tupla
tupla1 = 1, 2, 3
tupla2 = ()

# criando uma lista
lista1 = list()
lista2 = []

# verificando o tipo
print('Tipo tupla1:', type(tupla1))
print('Tipo tupla2:', type(tupla2))
print('Tipo lista1:', type(lista1))
print('Tipo lista2:', type(lista2))

# criando uma tupla mista
tupla_mista = (1, 2, 3.1415, 'a', 'isto é uma frase', [7, 8, 9])

# acessando elementos da tupla (slice / slicing)
## assim como listas, tuplas armazenam sequencias de objetos que podem ser acessados por suas posições
tupla_mista[0]  # acessando primeiro elemento
tupla_mista[-1]  # acessando último elemento
tupla_mista[1:3]  # o último índice é excludente
# nome_tupla[de onde: até onde: de quanto em quanto]

# tuplas são imutáveis
## isso significa que uma vez criadas, não podemos alterar, adicionar ou remover elementos da mesma
# contudo, se dentro da tupla houver uma lista, os elementos da lista podem ser alterados

# desempacotamento de tupla
nome, sobrenome, idade = ('gabi', 'sales', 27)

# tuplas são iteráveis
## por possuir os métodos __iter__ e __getitem__, tuplas podem ser iteradas
tuplas = (('gabi', 'sales'), ('jhonatas', 'antonelli'))
for nome, sobrenome in tuplas:
    print(nome, sobrenome)

# convertendo listas para tuplas
tuple(lista1)

# convertendo tuplas para listas
list(tupla1)

"""
Exercício:

1. Crie uma lista de compras com 5 elementos
2. Transforme a lista em tupla
3. Imprima os 3 elementos centrais utilizando slice
4. Itere sobre os itens da tupla e imprima: o nome do item e quantas letras ele possui
"""

lista_compras = []
print('Inserindo itens na lista de compras:')
for item in range(5):
    lista_compras.append(input(f'{item+1}º item: '))

print('-' * 20)
print('{:^20}'.format('LISTA DE COMPRAS'))
print('-' * 20)
print(lista_compras)
print(tuple(lista_compras))
print(lista_compras)
tupla_compras = tuple(lista_compras)
print(tupla_compras)
print(lista_compras)

print('3 elementos centrais:', tupla_compras[1:4])

for item in tupla_compras:
    print(item, '- nº de letras:', len(item))
