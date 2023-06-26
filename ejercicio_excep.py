try:
    num1 = int(input("Digite un numero: "))
    num2 = int(input("Digite otro numero: "))
    resultado = num1 / num2
except Exception as error:
    print("No se puede tener 0 en el divisor, Por favor digite un numero mayor a 0 en el divisor",error)
else:
    print("El resultado es: ",resultado)                