class Animal:
    def __init__(self,tipo,color,edad) -> None:
        self._tipo = tipo
        self._color = color
        self._edad = edad

    @property
    def get_tipo(self):
        return self._tipo
    
    @get_tipo.setter
    def get_tipo(self,tipo):
        self._tipo = tipo

    @property
    def get_color(self):
        return self._color

    @get_color.setter
    def get_color(self,color):
        self._color = color

    @property
    def get_edad(self):
        return self._edad

    @get_edad.setter
    def get_edad(self,edad):
        self._edad = edad

    def __str__(self) -> str:
        return f"El animal es de tipo: ({self._tipo}) tiene color: ({self._color}) y tiene una edad de: ({self._edad})"

animal1 = Animal("Perro","Negro",10)
print(animal1)            

        