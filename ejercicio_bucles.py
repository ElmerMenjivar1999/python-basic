numero = int(input("Digite el numero de la tabla de multiplicar: "))
numero2 = int(input("Digite otro numero de la tabla de multiplicar: "))
print("\n")
valor = 1
print(f"TABLA DEL {numero}\t\tTABLA DEL {numero2}")
for valor in range(1,11):
    print(f"{numero} X {valor} = {valor * numero}\t\t{numero2} X {valor} = {valor * numero2}")
print("\n")   