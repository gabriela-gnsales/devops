"""
Temos nativamente em python as seguintes estruturas de dados (containers):

1. list: lista
2. tuple: tupla
3. set: conjunto
4. dict: dicionário


Podemos avaliar cada estrutura e compará-las pelos seguintes critérios:
1. se é sequencia
    significa que tem o conceito de posição, onde podemos acessar os elementos pelos seus índices utilizando
    o slice. Para que o slice seja possível, deve possuir o método __getitem__ implementado.
    Consigo indexar (organizar em forma de índice) pela posição.

2. se é mutável
    uma vez criado o container, podemos alterar, adicionar ou remover elementos.

3. se é iterável
    podemos passar o container por um laço for e ter acesso a cada elemento. Para que a iteração seja possível,
    deve possuir o método __iter__ implementado.

4. se permite dados duplicados
    a estrutura set remove os duplicados, enquanto que os demais não

"""