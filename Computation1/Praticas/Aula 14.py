#exercicio 1

counter = 0

while counter < 10:
    counter += 1
    print(counter)

#exercicio 2

resultado = 0
multi = 0

while multi < 10:
    resultado += 2
    multi += 1
    print(f"2 * {multi} = {resultado}")

#exercicio 3


int1 = int(input("Input one int:"))
int2 = int(input("Input another int:"))
counterE = 0
counterC = 1

while counterE < int2:
    counterE += 1
    counterC *= int1

print(counterC)

#exercicio 4

intask = int(input("How many ints would you like to input?:"))
counter4 = 0
list4 = []

while counter4 < intask:
    counter4 += 1
    inputint = int(input(f"Int {counter4}:"))
    list4.append(inputint)

for i in list4:
    if i % 2 == 0:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")

#exercicio 5

resultado = 0
counter5 = 0

while resultado < 100:
    counter5 += 1
    input5 = int(input(f"Int{counter5}:"))
    resultado += input5

print(resultado)