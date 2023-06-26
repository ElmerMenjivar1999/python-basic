num = int(input("Digite un numero: "))
output = []

for i in range(1,num+1):
    divisible_by_3 = (i % 3 == 0)
    divisible_by_5 = (i % 5 == 0)

    if divisible_by_3 and divisible_by_5:
        output.append("FizzBuzz")
    elif divisible_by_3:
        output.append("Fizz")
    elif divisible_by_5:
        output.append("Buzz")
    else:
        output.append(str(i))

print(output)