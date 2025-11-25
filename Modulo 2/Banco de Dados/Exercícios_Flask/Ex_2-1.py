from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('ex_2-1.html')

@app.route('/sobre')
def sobre():
    return 'Olá, sou o monstro da prog. Aluno de python'


@app.route('/github')
def logar():
    return 'Voce entrou no github.'

if __name__ == '__main__':
    app.run(debug=True)
