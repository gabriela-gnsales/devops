from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return '<h1>Gritando na tela uhuul!</h1>'

@app.route('/boanoite')
def boa_noite():
    return '<h1>Não durmam antes do fim da aula!</h1>'