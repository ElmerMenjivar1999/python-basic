#Hacer una funcion que devuelva un texto en mayuscula

def mayuscula(text):
    return text.upper()

result = mayuscula("elmer")
print(result)

def loop_range(init_number,final_number):
    pares = []
    for number in range(init_number,final_number):
        if number % 2 == 0:
            pares.append(number)
            print(pares)

loop_range(1,11)

 
