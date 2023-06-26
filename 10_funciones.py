#Funciones
#Definimos una funcion

def my_function ():
    print("Esto es una funcion")

my_function()
my_function()
my_function()

def sum_two_values(first_number,second_number):
    print(first_number + second_number)   

sum_two_values(5,7)
sum_two_values(54754,71231)
sum_two_values("5","7")
sum_two_values(1.4,5.2)


#Retorno de valores

def sum_two_values_return(first_values,second_values):
    return first_values + second_values

my_result = sum_two_values_return(10,5)
# my_result = sum_two_values(10,10)
print(my_result)

def print_name(name,surname):
    print(f"{name} {surname}")

print_name("Elmer","Menjivar")

#Valores por defecto en una funcion
def print_name_default(name,surname,alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

#Se puede llamar la funcion sin el parametro que tiene el valor por defecto
print_name_default("Elmer","Menjivar")

#Con el asterisco se pueden poner los parametros que queramos
def print_texts(*text):
    print(text)

print_texts("Hola","Python","Pache")