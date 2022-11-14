"""
### Conjunto (set) ###

definição: é um container que armazena itens não ordenados/sequenciados, mutáveis e iteráveis
mas sem elementos duplicados.
"""

# criando um conjunto
conj = {1, 2, 3, 4, 5}
conj_vazio = set()
conj_vazio_errado = {}  # o tipo fica igual a dicionário

# verificando o tipo
print(type(conj))  # tipo set
print(type(conj_vazio))
print(type(conj_vazio_errado))

# criando um conjunto misto
misto = {1, 2, 3.1415, 'a', (1, 2, 3)}  # só pode elementos que não alteram, tuplas podem, listas e dicionários não
print(misto)

misto2 = {1, 2, '!', (1, 2, 3)}
print(misto2)

# acessando elementos do conjunto (slice / slicing)
## diferente de listas e tuplas, conjuntos são objetos não sequenciais, ou seja, não tem uma posição
## definida, o que impossibilita realizar o slice.

# conj[0]  # ocorre TypeError, não conseguimos acessar posições

## realizando a instrospecção do objeto set, observamos que não possui o método __getitem__, logo não temos acesso ao slice do objeto

# conjuntos são mutáveis
## podemos adicionar e remover elementos

## método add
conj.add(15)

## método remove
conj.remove(3)  # informo o valor que quero remover, não sua posição

# conjuntos são iteráveis
# porque tem o método get __iter__
for i in conj:
    print(i)

# conjuntos remove duplicados
lista = [1, 2, 3, 2, 3, 1, 5, 5, 4]
print(set(lista))

# Operações de conjunto
A = {1, 2, 3, 4, 5}
B = {1, 3, 5, 7, 9}

## interseção
A.intersection(B)

## união
A.union(B)

## diferença
A - B

## diferença simétrica
A.symmetric_difference(B)

## disjunção
A.isdisjoint(B)

"""
Exercício:

1. Gere um conjunto com 20 números aleatórios entre 1 e 25
2. Gere um segundo conjunto com 20 números aleatórios entre 5 e 30
3. Calcule:
    3.1. se são conjuntos disjuntos
    3.2. a interseção
    3.3. a união
    3.4. a diferença simétrica
    
Para geração dos números aleatórios, utilize a função nativa do python:

    import random
    random.randint(inicio, fim)

"""

from random import randint

conj1 = set()
conj2 = set()
cont = 0
while cont != 20:
    item_conj1 = randint(1, 25)
    item_conj2 = randint(5, 30)
    if item_conj1 not in conj1 and item_conj2 not in conj2:
        conj1.add(item_conj1)
        conj2.add(item_conj2)
        cont += 1

print('Conjunto com 20 números aleatórios entre 1 e 25:', conj1)
print('Conjunto com 20 números aleatórios entre 5 e 30:', conj2)

print('Conjunto 1 (20 números aleatórios entre 1 e 25):')
for pos, item in enumerate(conj1):
    print(f'{pos+1}º: {item}')

print('Conjunto 2 (20 números aleatórios entre 5 e 30):')
for pos, item in enumerate(conj2):
    print(f'{pos+1}º: {item}')

print('Conjunto 1 e conjunto 2 são disjuntos:', conj1.isdisjoint(conj2))
print('Interseçao conjunto 1 e conjunto 2:', conj1.intersection(conj2))
print('União conjunto 1 e conjunto 2:', conj1.union(conj2))
print('Diferença simétrica conjunto 1 e conjunto 2:', conj1.symmetric_difference(conj2))
