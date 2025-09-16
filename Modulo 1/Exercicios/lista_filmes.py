print('Digite o nome de 3 filmes para adicionar na lista.  ')
cont =1
nome =  []


while cont <=3: 
    filme = (input(f'Digite o nome do {cont} filme: '))
    nome.append(filme)
    cont = cont+1

print(nome)