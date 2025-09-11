from colorama  import init, Fore
init(autoreset=True)



print ("|-----------------------|")

print ("SISTEMA DE PROVAS")
print("|-----------------------|")

nome =(input("Nome do aluno: "))
nota1 =(int(input("Nota da primeira prova: ")))
nota2 =(int(input("Nota da segunda prova: ")))
nota3 =(int(input("Nota da terceira prova: ")))

print ("|-----------------------|")
media = (nota1+ nota2 + nota3)/3
if media>=5: 
    print(Fore.GREEN+'aluno foi aprovado')
else:
    print(Fore.RED+'Aluno foi reprovado')