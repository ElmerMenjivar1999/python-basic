#variables
my_variable = "My String variable"
print(my_variable)

my_int_variable = 10
int_convert_str = str(my_int_variable)
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

#concatenacion de variables
print(my_variable, int_convert_str, my_bool_variable)
print(type(int_convert_str))
print("Este es el valor de: ",my_int_variable)

#Funciones del sistema
print(len(my_variable))

#Variables en una sola linea
name, surname,alias,edad = 'Elmer','Menjivar','pache',35
print("Me llamo",name,surname,"y mi alias es: ",alias," Y tengo",edad,"de edad")

#entrada de datos
first_name = input("Cual es tu nombre? ")
age = input(" Cual es tu edad? ")

print(first_name)
print(age)

#Forzamos el tipo? 
address: str = "Mi direccion"
address = 23
print(type(address))#tipo int
