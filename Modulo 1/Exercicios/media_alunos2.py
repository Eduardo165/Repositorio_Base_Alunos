

print ('|------- SISTEMA DE PROVAS -------|')



numero_de_provas = int(input(' Digite a quantidade de provas : '))
contador = 1
soma = 0
while contador <= numero_de_provas:
    prova = float(input(f'Qual é a nota da prova {contador} '))
    contador = contador +1
    soma = soma + prova

media = soma / numero_de_provas
print(f'A soma é: {media}')
    

