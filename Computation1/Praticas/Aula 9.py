#exercicio 1

favcol = input("Tell me your favorite color:")

if favcol.lower() == "yellow":
    print("I cant support you!")
else:
    print("I can see why insert color here would be appealing to you")

#exercicio 2

import math

inputnum = int(input("Give me an Int number please:"))

inputnumf = float(inputnum)

if inputnumf < 0:
    print("The number inserted is negative.")
elif inputnumf >= 0:
    print(f"The square root of {inputnum} is: ", math.sqrt(inputnumf))

#exercicio 3

name = input("What is your name:")

cereal = input(f"Ok {name}, should the milk be added before the cereal? (Answear with True or False):")

if cereal.lower() == "true":
    print("You will fail computation 1!")
elif cereal.lower() == "false":
    print("You might pass computation 1!")

#exercicio 4

numa = float(input("a) Dá me um número:"))
numb = float(input("b) Dá me outro número:"))

operation = input("Seleciona 1 se quiseres multiplicar, 2 para somar e 3 para fazer a^b:" )

if operation == "1":
    print(numa * numb)
elif operation == "2":
    print(numa + numb)
elif operation == "3":
    print(numa ** numb)

#exercicio 5

gert1 = float(input("Gertrude went shooping for sodasn how many did she buy?:"))
gert2 = float(input("How much did she pay for each soda?:"))

fprice = gert1 * gert2

print(str(fprice) + "€")

if fprice > 10:
    print("She spent too much.")
else:
    print("She was within the budget")

if gert1 > 5:
    print("She bought too much soda!")