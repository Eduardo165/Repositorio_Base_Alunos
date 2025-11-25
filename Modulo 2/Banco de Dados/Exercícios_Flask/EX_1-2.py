from flask import Flask 

app =  Flask(__name__)


@app.route('/')
def index():
    return 'Ola mundo'

@app.route('/sobre')
def sobre():
    return'Ola, sou programador em python'

if __name__ =='__main__':
    app.run(debug=True)