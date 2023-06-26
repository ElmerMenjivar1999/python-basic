numero_notas = int(input("Digite el numero de notas que quiere registrar: "))
alumno = 0
suma_nota = 0
promedio = 0
while alumno < numero_notas:
    nota = int(input("Digite su nota: "))
    alumno += 1
    suma_nota += nota
promedio = suma_nota / numero_notas

print("El promedio del alumno es: ",promedio)