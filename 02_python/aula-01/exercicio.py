print('*' * 40)
print('{:^40}'.format('FORMULÁRIO'))
print('*' * 40)

nome = input('Nome: ').strip().capitalize()
cpf = int(input('CPF: '))
endereco = input('Endereço: ').strip()
idade = int(input('Idade: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))
telefone = int(input('Telefone: '))

print('*' * 40)

print(f'O seu nome é {nome}, você possui o CPF {cpf}, mora em {endereco}, possui {idade} anos, sua altura é {altura} metros e seu telefone é {telefone}.')

if idade >= 18 and peso >= 60 and altura >= 1.6:
    print('Você está apto para servir ao exército.')
else:
    print('Você não está apto.')

# print(
#   'Você está apta a servir no Exército!'
#   if idade >= 18 and peso >= 60 and altura >= 1.6
#   else ('Você não está apta!')
# )
