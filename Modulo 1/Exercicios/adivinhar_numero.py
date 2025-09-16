from random import randint


numero = randint(1,10)

print('|---------------MAGICA DO DUZEIRA---------------|')





print('Vou pensar em um numero.')
numero1 = int(input('Digite um numero de 1 a 10: '))


while numero1 != numero:
    print ('Voce errou.')
    if numero1 < numero:
        print('Numero maior. 👆')
    else:
        print('Numero menor. 👇')
    numero1 = int(input('Digite um numero de 1 a 10: '))
print('Voce acertou. 👌')

print('|------------------------------------------------|')