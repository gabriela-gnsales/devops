'''
Lista de compras
'''

lista_compras = list()

while True:
    item = input('Qual item deseja inserir na lista de compras [informe 0 para parar]? ').strip().lower()
    if item == '0':
        break
    lista_compras.append(item)

print('Lista de compras:', lista_compras)

lista_compras2 = []
num_itens = int(input('Quantos itens precisa comprar? '))

for i in range(num_itens):
    item = input(f'{i+1}º item: ').strip().lower()
    lista_compras2.append(item)

print('-' * 20)
print('LISTA DE COMPRAS:')
print('-' * 20)
for item in lista_compras2:
    print(item)
print('-' * 20)
