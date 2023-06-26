dividendo = int(input("Digite el numero dividendo: "))
divisor = int(input("Digite el numero divisor: "))


if divisor == 0:
    print("No puede dividir con un numero 0",ZeroDivisionError)
else:
    division = dividendo / divisor
    print("La division de los dos numeros es: ",division)    
