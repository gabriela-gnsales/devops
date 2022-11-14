# Recurso do PyCharm para colocar avisos/lembretes no código, ele é acessado na guia inferior
# ToDo: preciso melhorar esse método

if not True:
    print('Entrou no if.')
else:
    print('Entrou no else.')

lista = [1, 2, 3]
lista.pop(1)
print(lista)

# método POP remove um elemento da lista, se não passar nenhum índice ele remove o último por padrão

print("alguma frase aleatória"[::-1])

texto = 'saudARDE'
separar_texto = texto.split('A')
print(separar_texto)
print(type(texto))
print(dir(texto))  # métodos da classe que a variável 'texto' se enquadra, isto é, a classe 'str'

# tudo em python é um objeto
# as classes string e lista possuem alguns métodos iguais
# para ver todos os métodos que a classe implementa: dir(classe) - ex: dir(lista)
# INTROSPECÇÃO: conceito
# GERADORES: conceito onde consigo criar meu próprio iterador
# o objeto é iterável quando implementa o método ITER e/ou GETITEM
# DUCK TYPING: conceito tipagem pato

# VENV: ambiente virtual isolado
# ideal para evitar incompatibilidades de versões do python...
# reduzir tamanho de executáveis, pois eles encapsulam todas as bibliotecas

# PIP: gerenciador de pacotes do python

# PARA EXECUTAR DE FORMA ITERATIVA INSTALAR IPYTHON:
# pip install ipython
# ipython -i nome_arquivo.py
