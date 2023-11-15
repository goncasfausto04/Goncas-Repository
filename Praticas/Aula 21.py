#exercicio 1

inputint = input("How many items in your list?:")

while not inputint.isdigit() or not int(inputint) != 0:
    inputint = input("Input a number:")

list = [int(input("Num:")) for i in range(int(inputint))]
listmin = list[0]

for i in list[1:]:
    if i < listmin:
        listmin = i

print(listmin)

#exercicio 2
import math

inputopt = input("What option you whant?:")
opt = ["1", "2", "3"]

while inputopt not in opt:
    inputopt = input("Input a number:")

if inputopt == "1":
    strinput = input("String:").upper()
    print(strinput)

if inputopt == "2":
    colorfav = input("What is your fav color?")
    print("Horrible choice.")

if inputopt == "3":
    print(f"Here is a pice of pie: {math.pi}")

#exercicio 3
wordinput = input("Input a word please:")


while len(wordinput) != 4 or "a" not in wordinput.lower():
    wordinput = input("Input a word please:")

print(wordinput[::-1])

#exercicio 4
import numpy

lista = [int(input(f"Input {i + 1}:")) for i in range(4)]

listamatrix = [lista[0:2], lista[2:]]
print(numpy.array(listamatrix))

determinante = (lista[0] * lista[3]) -(lista[1] * lista[2])

print(f"The determinant of the matrix is: {determinante}.")