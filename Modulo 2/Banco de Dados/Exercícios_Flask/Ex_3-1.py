from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    nome = 'eduardo'
    sobrenome = 'gomes'
    return render_template('ex_3-1.html',nome = nome , sobrenome=sobrenome)








if __name__ == '__main__': 
    app.run(debug=True) 