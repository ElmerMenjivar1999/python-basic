#Loops, bucles, ciclos

# Bucle While

# my_condition = 0

# while my_condition < 10:
#     print(my_condition)
#     my_condition += 2
# else:#Es opcional
#     print("Mi condicion es mayor o igual que 10")

# print("La ejecucion continua")

# while my_condition < 20:
#     my_condition += 1
#     if my_condition == 15:
#         print("Se detiene la ejecucion")
#         break
#     print("Mi condicion es menor que 20" ,my_condition)

# print("La ejecucion continua")

#Bucle For

my_list = [35,24,62,52,30,30,17]

for element in my_list:
    print(element)

my_tuple = (35,1.77,"Elmer","Menjivar","Elmer")
my_set = {"Elmer","Menjivar",23}
my_dict = {"Nombre":"Elmer","Apellido":"Menjivar","Edad":23}

for element in my_tuple:
    print(element)

for element in my_set:
    print(element)

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
else:
    print("El bucle for para mi diccionario ha finalizado")      