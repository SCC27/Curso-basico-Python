def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")




menu = """
Bienvenido al conversor de monedad 🔁

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion:
"""
opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3875)

elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion ==3:
    conversor("Mexicanos", 24)
else:
    print("Elige una opcion correcta porfavor")

