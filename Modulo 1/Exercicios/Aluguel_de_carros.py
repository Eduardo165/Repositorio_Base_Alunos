print ("ALUGUEL DE CARROS")
dias=int(input("Por quantos dias o carro foi alugado? "))
km=int(input("Quantos km o carro rodou? "))
total_dias = dias*60
total_km =km*0.15
valor_total= total_dias + total_km
print(f"Voce andou {km} km por {dias} dias, entao o preço a pagar e R$ {valor_total}.")

