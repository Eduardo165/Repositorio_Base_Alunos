# EXERCICIO 4-1: Formulário simples com request.form
# Crie uma página com um formulário que envia um nome e retorna uma saudação personalizada com esse nome.

from flask import Flask, render_template, request

app =  Flask(__name__)


@app.route('/',  methods =['POST' , 'GET'])
def index():

    if  request.method == 'POST':
        nome = request.form['nome']

        return f'Salve {nome}'

    return render_template('ex_4-1.html')



if __name__ =='__main__':
    app.run(debug=True)