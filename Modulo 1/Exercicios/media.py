print ("|----------------------|")

print ("SISTEMA DE PROVAS")
print("|-----------------------|")

nome =(input("Nome do aluno: "))
nota1 =(int(input("Nota da primeira prova: ")))
nota2 =(int(input("Nota da segunda prova: ")))
nota3 =(int(input("Nota da terceira prova: ")))

print ("|-----------------------|")
media = (nota1+ nota2 + nota3)/3
print (f'aluno aprovado {media >=5}')