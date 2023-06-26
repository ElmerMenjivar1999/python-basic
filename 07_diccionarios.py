#Diccionarios
#Declarando diccinarios
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))
#Relacion Clave-Valor
my_other_dict = {"Nombre":"Elmer","Apellido":"Menjivar","Edad":23}
my_dict = {
    "Nombre":"Elmer",
    "Apellido":"Menjivar",
    "Edad":23,
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.75
}
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))
#Se acceden a los datos atravez de las claves
print(my_dict["Nombre"])
#Se actualizan los valores atravez de la clave
my_dict["Nombre"] = "Juan"
print(my_dict["Nombre"])

print(my_dict[1])
#Se anade un nuevo clave-valor al diccionario
my_dict["Calle"] = "Calle Portugal"
print(my_dict)
#Se elimina un elemento del diccionario especificando la clave
del my_dict["Calle"]
print(my_dict)
#Se busca por clave , no por valor
print("Elmer" in my_dict)#False
print("Apellido"in my_dict)
print(my_dict["Apellido"])
#Un listado con todo las claves y valores
print(my_dict.items())
print(my_dict.keys())#Solo retorna las claves
print(my_dict.values())#Solo retorna los valores
my_new_dict = dict.fromkeys(("Nombre",1))#Crea un diccionario sin valores
print(my_new_dict)
#Copia todas las claves del diccionario especificado al nuevo diccionario sin los valores
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
#Se meten datos por defecto en todas las claves
my_new_dict = dict.fromkeys(my_dict,("Elmer","M enjivar"))
print(my_new_dict)
