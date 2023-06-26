colores = {'rojo':'red','verde':'green','negro':'black'}

try:
    print("Llaves del diccionario")
    for key in colores.keys():
        print(key)

    color = input("Digite la llave en espanol para imprimir su valor en ingles: ")
    print(colores[color])
except:
    print("La llave introducida no existe en el diccionario")
