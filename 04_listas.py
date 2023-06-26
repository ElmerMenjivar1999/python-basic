#Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [23,24,62,52,30,30,17]
print(my_list)
print(len(my_list)) #tiene 7 elementos

my_other_list = [23,1.75,"Elmer","Menjivar"]
print(type(my_other_list))

#Accediento a los datos de la lista
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

print(my_list.count(30))#Contando cuantos elementos hay en la lista
# print(my_other_list[-5] indexError: Fuera de rango
# print(my_other_list[4]))indexError: Fuera de rango

age,height,name,surname = my_other_list
print(name)
#concatenando dos listas
print(my_list + my_other_list)
#Insertando un valor al final de la lista
my_other_list.append("Menjivar Corp")
print(my_other_list)
#insertando un valor en una posicion especificada 
my_other_list.insert(1,"Negro")
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

my_other_list.remove("Rojo")
print(my_other_list)


my_list.remove(30)
print(my_list)
#Eliminando el ultimo valor de la lista
print(my_list.pop()) #Se imprime el valor eliminado
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)

#Se elimina el valor de la lista especificando el id
del my_list[2]
print(my_list)
#copiando una lista a otra
my_new_list = my_list.copy()
print(my_new_list)
#La lista se revierte
my_new_list.reverse()
print(my_new_list)
#Ordenando de menor a mayor
my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list.clear()
print(my_list)

my_list = "Hola Python"
print(my_list) 
print(type(my_list))
