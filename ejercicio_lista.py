lista_usuario = []
lista_usuario_copy = []

longitud = int(input("Digite la longitud de la lista: "))

for i in range(longitud):
    valores = int(input("Digite el valor : "))
    lista_usuario.append(valores)

print("Su lista es: ",lista_usuario)

valor_eliminado = int(input("Digite el valor que quiera eliminar de la lista: "))
lista_usuario.remove(valor_eliminado)

print("El valor que elimino es: ",valor_eliminado)
print("Su nueva lista es: ",lista_usuario)

opcion = input("Desea copiar la lista a otra lista? si/no\n")
if opcion == "si" or opcion == "Si":
    lista_usuario_copy = lista_usuario.copy()
    print("La lista copiada es: ",lista_usuario_copy)
elif opcion == "no" or opcion == "No":
    print("Pasando a la siguiente pregunta.....")

actualizar_dato = input("Desea actualizar un dato en especifico si/no\n")

if actualizar_dato == "si" or actualizar_dato == "Si":
    print(lista_usuario,"\n")
    indice = int(input("Digite el indice del dato: "))
    dato = int(input("Digite el dato que quiera actualizar: "))
    dato_actualizado = int(input("Digite el dato que reemplaze al dato seleccionado: "))
    lista_usuario[indice] = dato_actualizado
    print("La lista modificada es: ",lista_usuario)
elif actualizar_dato == "no" or actualizar_dato == "No":
    print("Saliendo del programa......")
elemento = 0
id = 0
print("Indice \t\tValor")
for elemento in lista_usuario:
    print(id,"\t->","\t",elemento)
    id+=1    