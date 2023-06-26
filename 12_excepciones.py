#Excepciones

nomber_one,nomber_two = 5, 1

nomber_two = "1"
#try, except
try:
    print(nomber_one + nomber_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

#try,except,else,finally
else:#opcional
    #Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:#opcional
    #Se ejecuta siempre aunque hayga una excepcion
    print("La ejecucion continua")

# Excepciones por tipo
try:
    print(nomber_one + nomber_two)
    print("No se ha producido un error")
except TypeError:#Solo se ejecuta cuando hay un error de tipo typeError
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")

#Captura de la informacion de la excepcion
try:
    print(nomber_one + nomber_two)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as excepcion_error:
    print(excepcion_error)        