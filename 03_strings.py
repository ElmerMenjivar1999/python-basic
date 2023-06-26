#Strings

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " "+my_other_string)

my_new_line_string = "Este es un String \ncon saltlo de linea"
print(my_new_line_string)


my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_escape_string = "\tEste es un String escapado \n"
print(my_escape_string)

#Formateo
name, surname,age = "Elmer", "Menjivar", 23

print("Mi nombre es {} {} y mi edad es {} ".format(name,surname,age))
print("Mi nombre %s %s y mi edad es %d "%(name,surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age} ")

#Desempaquetado de caracteres
lenguage = "python"
a,b,c,d,e,f = lenguage
print(a)
print(b)

#Division

language_slice = lenguage[1:3]
print(language_slice)

language_slice = lenguage[1:]
print(language_slice)

language_slice = lenguage[-2]
print(language_slice)

language_slice = lenguage[0:6:2]
print(language_slice)

#Reverse
#invirtiendo el string
resersed_language = lenguage[::-1]
print(resersed_language)

#Funciones
#Poner primera letra en mayuscula
print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count("t"))
print(lenguage.isnumeric())
print("1".isnumeric())
print(lenguage.lower())

print(lenguage.lower().isupper())
print(lenguage.startswith("py"))