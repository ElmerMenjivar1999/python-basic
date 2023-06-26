#Tuplas
#Las tuplas son inmutables
#Definiendo una tupla

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35,1.77,"Elmer","Menjivar","Elmer")
my_other_tuple = (23,60,30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4])fuera de rango
# print(my_tuple[-6])
print(my_tuple.count("Elmer"))
print(my_tuple.index("Menjivar"))#Nos imprime el indice del valor especificado
print(my_tuple.index("Elmer"))
#Error no  puede cambiar el valor
# my_tuple[1] = 1.80
#Se pueden mezclar tuplas
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
#Se pueden mezclar elementos concretos
print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Menjivar Corp"
my_tuple.insert(1,"Negro")
print(my_tuple)
my_tuple = tuple(my_tuple)
print(tuple(my_tuple))
print(type(my_tuple))
#Borrando la tupla por completo
del my_tuple
print(my_tuple)