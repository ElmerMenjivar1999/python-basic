#Sets
#declarando los sets
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))#Inicialmente es un dicionario

my_other_set = {"Elmer","Menjivar",23}
print(type(my_other_set))#Ahora es un set

print(len(my_other_set))

my_other_set.add("Pache")#anadiendo datos al set
print(my_other_set) #un set no es una estructura ordenada

#Un set no admite datos repetidos
my_other_set.add("Pache")
print(my_other_set)
#Comprobando si existe el elemento en el set
print("Elmer" in my_other_set)#True
print("elmir" in my_other_set)#False
#Eliminando un elemento del set
my_other_set.remove("Elmer")
print(my_other_set)
#Elimina los elementos del set
my_other_set.clear()
print(my_other_set)
#Elimina el set por completo
del my_other_set
# print(my_other_set)

my_set = {"Elmer","Menjivar",23}
my_list = list(my_set)
print(my_list)
print(my_list[0])
#Uniendo dos sets
my_other_set = {"Javascript","Python","C++"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
#Quitando los elementos de my_set
print(my_new_set.difference(my_set))

