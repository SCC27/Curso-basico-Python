pesos = input("¿Cuantos pesos colonmbianos tienes?: ")
pesos = float(pesos)
valor_mexicano = 188.05
peso_mexicano = pesos / valor_mexicano
peso_mexicano = round(peso_mexicano, 2)
peso_mexicano = str(peso_mexicano)
print("Tienes $" + peso_mexicano + "pesos mexicanos")