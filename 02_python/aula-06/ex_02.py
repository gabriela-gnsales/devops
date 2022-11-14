'''
1. Crie um programa que leia um arquivo CSV;
2. Processe o arquivo removendo o campo ID;
3. Grave o resultado em um novo arquivo CSV.
'''

'''
from os.path import isfile, isdir

if isfile('cadastro.csv'):
    print('O arquivo "cadastro.csv" EXISTE.')
else:
    print('O arquivo "cadastro.csv" NÃO existe.')

print('O arquivo "cadastro.csv" existe?')
print('Sim' if isfile('cadastro.csv') else 'Não')

if isdir('../aula-05/'):
    print("O diretório EXISTE")
else:
    print("O diretório NÃO existe")
'''

with open('cadastro.csv', 'r', encoding='utf-8') as arquivo_leitura, \
     open('cadastro_saida.csv', 'w', encoding='utf-8') as arquivo_escrita:
    for linha in arquivo_leitura.readlines():
        dados = linha.split(', ')[1:]
        nova_linha = ', '.join(dados)
        arquivo_escrita.write(nova_linha)

# PROCURAR: .rstrip()

# MODO 2

# processado = []
# with open('cadastro.csv', 'r+') as arquivo_inicial:
#     linhas = arquivo_inicial.readlines()[1:]
#     for item in linhas:
#         dados = item.split(',')
#         # nome = dados[1]
#         # sobrenome = dados[2]
#         # email = dados[3].replace('\n', '')
#         # processado.append(f'{nome},{sobrenome},{email}\n')
#         processado.append(f'{dados[1]},{dados[2]},{dados[3]}')
# with open('cadastro_saida.csv', 'w') as arquivo_saida:
#     for item in processado:
#         arquivo_saida.write(item)

# MODO 3

# with open('cadastro.csv') as arquivo_inicial:
#     linhas = arquivo_inicial.readlines()
#     with open('novo_cadastro.csv', 'w') as arquivo_saida:
#         for linha in linhas:
#             _, nova_linha = linha.split(sep=',', maxsplit=1)
#             arquivo_saida.write(nova_linha)

# MODO 4

# with open('cadastro.csv', 'r', encoding='utf-8') as f_read, \
#      open('cadastro_saida.csv', 'w', encoding='utf-8') as f_write:
#     for linha in f_read.readlines():
#         lista = linha.split(',')[1:]
#         nova_linha = ','.join(lista)
#         f_write.write(nova_linha)

# MODO 5

# import csv
#
# with open('cadastro.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     with open('cadastro_saida.csv', 'w') as result:
#         writer = csv.writer(result)
#         for r in reader:
#             # Use CSV Index to remove a column from CSV
#             writer.writerow((r[1:4]))
