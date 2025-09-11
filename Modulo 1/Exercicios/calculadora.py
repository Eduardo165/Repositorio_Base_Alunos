
print("|-----------------------|")
print("Calculadora")
print("1- Soma")
print("2- Subtraçao")
print("3- Mutiplicaçao")
print("4- Divisao")
print("|------------------------|")

escolha= float(input("Escolha uma das opçoes: "))


numero1=float(input('Digite o primeiro  numero: '))
numero2=float(input("Digite o segundo numero: "))
if escolha==1:
    print(f"O resultado de {numero1}+{numero2} e {numero1+numero2}")
elif escolha==2:
    print(f"O Resultado de {numero1}-{numero2} e {numero1-numero2}")
elif escolha==3:
    print(f"O resultado de {numero1}x{numero2} e {numero1*numero2}")
elif escolha==4:
    print(f"O resultado de {numero1}/{numero2}e {numero1/numero2}")
else:
    print(" Erro, escolha um numero valido")