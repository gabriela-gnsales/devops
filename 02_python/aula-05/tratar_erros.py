def divide_numeros(dividendo, divisor):
    return dividendo/divisor

try:
    # num1 = input('Informe o primeiro número: ')
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
    resultado = divide_numeros(num1, num2)

# except ZeroDivisionError:
#     print('Divisão por ZERO não suportada.')
# except TypeError:
#     print('Erro de tipagem.')

# OUTRO MODO: passando 2 tipos de exceções em um mesmo código
except (ZeroDivisionError, TypeError) as exc:
    print(f'Divisão por zero não suportada OU erro de tipagem. ERROR: {exc}')

except Exception as erro:  # só com 'except' é um tratamento muito generalista, com o 'exception' dá para tratar um erro por vez, erro específico
    # código a ser executado se ocorrer um erro
    print(f'Um erro foi detectado! ERROR: {erro.__class__}')
else:
    # código a ser executado se não houver erros
    print(resultado)
finally:
    print('Programa finalizado...')

# easier to ask forgiveness than permission (EAFP)
# look before you leap (LBYL)

# EXERCÍCIO

cadastro = [
    'Adriele, 25, Desenvolvedor Web',
    'Gabriela, 35, Desenvolvedor BackEnd',
    'Leonardo, 29, DataScience',
    'Carlos, 33'
]

def dados_processados(cadastros):
    for cadastro in cadastros:
        dados = cadastro.split(',')

        if len(dados) != 3:
            raise ValueError('Formato de dados incorreto no cadastro.')
        nome = dados[0]
        idade = int(dados[1])
        cargo = dados[2]
        print(f'{nome} tem {idade} e exerce o papel de {cargo}.')
try:
    dados_processados(cadastro)
except ValueError as exc:
    print(f'O programa detectou o seguinte ERROR: {exc}')

# EXEMPLO

# s = 'apple'
# try:
#     num = int(s)
# except ValueError:
#     raise ValueError('String não pode ser convertido para inteiro.')
