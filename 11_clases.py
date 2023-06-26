#Clases

class MyPerson:
    pass #Es para no ejecutar nada

print(MyPerson)

class Person:
    def __init__(self,name,surname,alias = "Sin alias"):#Nos sirve para crear un constructor de clase
        self.name = name
        self.surname = surname
        self.alias = alias
    #Metodo de clase
    def walk(self):
        print(f"{self.name} {self.surname} {self.alias} Esta caminando")    

my_person = Person("Elmer","Menjivar")
print(f"{my_person.name} {my_person.surname}")
my_person.walk()

my_other_person = Person("Juan","Canales","Juanito")
print(my_other_person.name,my_other_person.surname,my_other_person.alias)
my_other_person.walk()
