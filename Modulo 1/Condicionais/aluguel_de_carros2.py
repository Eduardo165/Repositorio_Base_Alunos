print("------------------")
print("ALUGUEL DE CARRO")
print("------------------")
modelo=input('Qual o modelo de carro? ')
dias=int(input("quantos dia vai alugar o carro: "))
km=float(input('quantos km o carro rodou: '))

if modelo== 'kiwid':
    diaria=50

elif modelo== 'ford ka':
    diaria=55

elif modelo== 'bmw':
    diaria=100
else:
    diaria=60
total_dias=dias*diaria
total_km=km*0.79
valor_total=total_dias+total_dias
print (f'Voce percorreu {km}km por {dias} dias, entao o preço a pagar sera {valor_total}') 
