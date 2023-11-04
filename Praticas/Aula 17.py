#exercicio 1

for i in range(5):
    for j in range(3):
        print("*", end="")
    print()

#exercicio 2

listint = [i for i in range(1,21)]

print(listint)

listint2 = [i**2 for i in listint]

print(listint2)

#exercicio 3

listcoiso = [int(input("Enter a number: ")) for _ in range(4)]

number = listcoiso[0]

for i in listcoiso[1:]:
    if i > number:
        number = i

print("The maximum number is:", number)

#exercicio 4

listint = [int(input("Enter a number: ")) for ite in range(4)]

highcouter = 0

for i in listint:
    if i > 600:
        highcouter += 1

if highcouter >= 1:
    print("HIGH")

#ou

listinte = [int(input("Enter a number: ")) for ite in range(4)]
high = False

for i in listinte:
    if i > 600:
        high = True

if high == True:
    print("HIGH")