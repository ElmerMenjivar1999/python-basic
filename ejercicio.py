lista_valores = []
lista_pares = []
lista_impares = []

longitud = int(input("Digite la longitud de la lista: "))

for i in range(longitud):
    valores = int(input("Digite el valor: "))
    lista_valores.append(valores)

for elemento in lista_valores:
    if elemento % 2 == 0:
        lista_pares.append(elemento)
    else:
        lista_impares.append(elemento)
           
print(f"Los elementos pares de la lista son = {lista_pares}")
print(f"Los elementos impares de la losta son = {lista_impares}")
