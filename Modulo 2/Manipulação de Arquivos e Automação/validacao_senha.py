import json

with open('senha.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

email = input('Digite o seu email: ')
senha = input('Digite a sua senha: ')

if email == dados['email'] and senha == dados['senha']:
    print('Acesso liberado!')
else:
    print('Acesso negado!')