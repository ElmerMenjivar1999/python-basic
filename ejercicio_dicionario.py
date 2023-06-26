datos = {"Nombre":"Juan","Apellido":"Canales","Edad":35,"Direccion":"Calle Portugal"}
print("Claves de los datos",datos.keys())

obtener_dato = input("Que dato quiere obtener? ")


print(f"El dato que solicito es {obtener_dato.capitalize()} : {datos[obtener_dato.capitalize()]}")

opcion = input("Quiere ver todo sus datos? si/no: ")

if opcion == 'Si' or opcion == 'si':
    print(datos.items())

actualizar_dato = input("Quiere actualizar un dato? si/no: ")

if actualizar_dato == 'Si' or actualizar_dato == 'si':
    clave = input("Digite la clave para actualizar el dato: ")
    nuevo_dato = input("Digite el nuevo dato: ")
    datos[clave.capitalize()] = nuevo_dato.capitalize()
    print("Los nuevos datos son: ",datos) 

print("Creando un nuevo diccionario".center(10,"-"))
nuevo_diccionario = dict.fromkeys(datos)
print("Nuevo diccionario sin datos: ",nuevo_diccionario)
