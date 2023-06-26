try:
    lista = [1,2,3,4,5]
    indice = int(input("Digite un indice para imprimir el valor: "))
    print("El valor que esta en el indice especificado es: ",lista[indice])
except Exception as Error:
    print("El indice que digitó no se encuentra en la lista ",Error) 
    print("Por favor digite un indice del 0 - 4")   