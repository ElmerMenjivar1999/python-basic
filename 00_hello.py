#print(type("Hola mundo"))
"""
comentario 
en varias
lineas

"""
listaValores = []
def maxYMinNumero(lista) -> list:
    return f" \nLa lista completa es {lista}, \nEl numero menor de la lista es: {min(lista)} y el numero mayor es: {max(lista)}"

longitud = int(input("Digite una longitud: "))

for i in range(longitud):
    valores = int(input(f"Digite el valor {i+1}: "))
    listaValores.append(valores)

print(maxYMinNumero(listaValores))



