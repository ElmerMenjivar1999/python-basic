class Person:
    def __init__(self,first_name,last_name) :
        self.__first_name = first_name
        self.__last_name = last_name
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    @property
    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

my_person = Person("Elmer","Menjivar")
# print(my_person.get_first_name())
print(my_person.get_last_name())
print(my_person.get_full_name)
# my_person.__first_name = "Alberto"
my_person.__last_name = "Rivera"
# print(my_person.__first_name,my_person.__last_name)

#Aplicando Herencia
class Empleado(Person):
    def __init__(self, first_name, last_name,sueldo):
        super().__init__(first_name, last_name)
        self.sueldo = sueldo

    def mostrar_detalles(self):
        return f"[Nombre Completo: {self.get_full_name}, Sueldo: {self.sueldo}$]"
    
    def sueldo_minimo(self):
        if self.sueldo >= 10000:
            print(f"El empleado {self.get_full_name} tiene el sueldo minimo")
        else:
            print(f"El empleado {self.get_full_name} necesita un aumento")


empleado1 = Empleado("Lucia","Menjivar",10000)
print(empleado1.mostrar_detalles())
print(empleado1.sueldo_minimo())  
empleado2 = Empleado("David","Herrera",8000)
print(empleado2.mostrar_detalles())
print(empleado2.sueldo_minimo())      

