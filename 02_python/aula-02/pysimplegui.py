import PySimpleGUI as sg

layout = [
    [sg.Text('Qual o seu nome?')],
    [sg.InputText(key='nome_usuario')],
    [sg.Button('Enviar')],
    [sg.Text('', key='texto_usuario')],
]

janela = sg.Window('PySimpleGUI', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    # if evento == 'Enviar':
    #     resultado = valores['nome_usuario']
    #     janela['texto_usuario'].update((f'Bem vindo, {resultado}!'))
    resultado = valores['nome_usuario']
    janela['texto_usuario'].update((f'Bem vindo, {resultado}!'))
janela.close()
