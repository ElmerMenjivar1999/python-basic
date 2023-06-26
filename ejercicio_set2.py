set = {"Elmer","Menjivar",23,1.75}
otro_set = {"Banana","Fresa","Manzana","Uva","Elmer","Menjivar"}

otro_set.remove("Menjivar")
set.add("Banana")
set.add("Fresa")
#Devuelve el numero de elementos en comun entre dos sets
print(len(set.intersection(otro_set)))
