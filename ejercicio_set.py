set = {"Elmer","Menjivar",23,1.75}
otro_set = {"Banana","Fresa","Manzana","Uva","Elmer","Menjivar"}

set.discard("Elmer")
print(set)
set.pop()
print(set)

nuevo_set = set.union(otro_set)
print(nuevo_set)
#Se elimina los elementos del otro set
set.difference_update(otro_set)
print(set)
#Copiando un set a otro
copia_set = set.copy()

print(copia_set)

interseccion_set = len(set.intersection(otro_set))
print(interseccion_set)