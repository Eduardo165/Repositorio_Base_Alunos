from flask import Flask 

app =  Flask(__name__)


@app.route('/')
def index():
    return 'Ola mundo'

@app.route('/sobre')
def sobre():
    return'Ola, sou programador em python'


@app.route('/ola/<nome>')
def ola(nome):
    if nome == 'eduardo':
        return f'Ola melhor do mundo!'
    else:
        return f'Ola {nome}'


@app.route('/dobro/<numero>')
def dobro(numero):
    numero = int(numero)
    return f'O dobro do {numero} é: {numero*2} '

if __name__ =='__main__':
    app.run(debug=True)