### FUNÇÕES

# 1. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
# formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

data = input('Escreva a data (desta forma DD/MM/AAAA): ')

mes = {'01':'janeiro',
       '02':'fevereiro',
       '03':'março',
       '04':'abril',
       '05':'maio',
       '06':'junho',
       '07':'julho',
       '08':'agosto',
       '09':'setembro',
       '10':'outubro',
       '11':'novembro',
       '12':'dezembro'}


def processa_data(data):
    try:
        data_lista = data.split('/')
        if int(data_lista[0]) > 0 and int(data_lista[0]) < 32 and int(data_lista[1]) > 0 and int(data_lista[0]) < 13 and int(data_lista[2]) > 0:
            print(f'{data_lista[0]} de {mes[data_lista[1]]} de {data_lista[2]}')
    except:
        print('NULL')


processa_data(data)
