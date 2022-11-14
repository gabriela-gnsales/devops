"""
### Dicionário (dict) ###

definição: é um container que armazena elementos/objetos de forma
não sequencial, mutável e iterável, permitindo valores repetidos, mas não chaves
"""

# criando um dicionário
dicio = {'a': 1, 'b': 2, 'c': 3}

# verificando o tipo
print(type(dicio))

# criando um dicionario complexo
complex = {
    'inteiro': 8,
    'float': 3.1415,
    'string': 'um texto qualquer',
    'lista': [1, 2, 3],
    'tupla': (1, 6, 22),
    'dicio': {
        'rua': 'nome da rua',
        'numero': '123',
    }
}

print(complex)

# acessando os elementos do dicionário
## diferente de listas e tuplas, o acesso não é posicional, mas pela chave
dicio['a']
complex['float']

# dicionários são mutáveis
## podemos adicionar e remover elementos, podemos alterar valores mas não as chaves
complex['dicio']['numero'] = 360
complex['lista'].append(4)
complex['dicio']['bairro'] = 'CIC'
# para remover um elemento
del complex['string']
complex.pop('inteiro')
complex['dicio'].pop('numero')

# dicionários são iteráveis
for key in complex:
    print(key)  # desse jeito retorna apenas a chave

for key in complex:
    print(f'{key} = {complex[key]}')

# outra forma de iteração:
for key, value in complex.items():
    print(key, value)

# métodos de dicionário
## novo dicionário de compras contendo item e quantidade

compras = {
    'arroz': 1,
    'feijão': 3,
    'chocolate': 2,
    'requeijão': 4
}

## método keys
compras.keys()

## método values
compras.values()

## método items
compras.items()

## verificando de tem um item no dicionario
'abobrinha' in compras.keys()
