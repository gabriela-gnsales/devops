### MÓDULOS

# 1. Crie um sistema modular que calcule área de 3 formas geométricas. O sistema deve conter:
#       a. um arquivo principal chamado 'main.py' contendo o menu do sistema.
#       b. o menu deve ter 4 opções: sendo as 3 primeiras para cálculo das formas geometricas e a última para
#          encerrar a execução
#       c. um móludo chamado 'geometria.py' contendo as fórmulas de cálculo das áreas

import geometria

forma = input('Escolha uma forma geométrica (quadrado, circulo e triangulo) ou digite sair: ')

if forma == 'quadrado':
    lado = float(input('Digite o lado de seu quadro: '))
    print(geometria.area_quadrado(lado))

elif forma == 'circulo':
    raio = float(input('Digite o raio de seu circulo: '))
    print(geometria.area_circulo(raio))

elif forma == 'triangulo':
    base = float(input('Digite a base de seu triangulo: '))
    altura = float(input('Digite a altura de seu triangulo: '))
    print(geometria.area_triangulo(base,altura))

else:
    print('Você colocou algum parâmetro errado ou encerrou sua sessão.')
