nombre = input("Digite su nombre: ")
print("Su nombre es: ",nombre)
comienzo_nombre = input("\nCon que caracteres comienza su  nombre: ")

if nombre.startswith(comienzo_nombre):
    print(f"Correcto!, su nombre comienza con '{comienzo_nombre}'")
else:
    print(f"Incorrecto!, su nombre no comienza con '{comienzo_nombre}' \nSu nombre comienza con '{nombre[0:2]}'")
