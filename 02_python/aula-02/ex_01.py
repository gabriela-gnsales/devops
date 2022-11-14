# Exercício Aula 02 - Listas
'''
Dada a lista a seguir:
valores = [23, 18, 45, 78, 55, 64, 16]
Crie um script Python que informe qual a posição do **MAIOR** elemento que esta dentro da lista.
'''

valores = [23, 18, 45, 78, 55, 64, 16]

maior = max(valores)
posicao = valores.index(maior)

print(f'O maior valor dessa lista é {maior} e está na {posicao+1}ª posição.')




