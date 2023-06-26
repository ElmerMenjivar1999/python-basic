tupla = (8,8,8,6,7,7,9,0,0,1)
id = 0
for i in tupla:
    print(f"{id} -> {i}")
    id+=1

valor = int(input("Digite el valor para saber cuanto se repite en la tupla: "))

print(f"El valor introducido se repite {tupla.count(valor)} veces")

elemento = int(input("Digite un valor de la tupla para conocer su indice: "))

print(f"El indice de {elemento} es {tupla.index(elemento)}")
