pesos = input("¿Cuantos pesos mexicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 20.65
peso_mexicano = pesos / valor_dolar
peso_mexicano = round(peso_mexicano, 2)
peso_mexicano = str(peso_mexicano)
print("Tienes $" + peso_mexicano + " dolares")