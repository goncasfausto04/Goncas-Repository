#exercicio 1

def printmy(a):
    return print(a)

string = input("Input:")

printmy(string)

#exercicio 2

def funca(var,list):
    count = 0
    index = []
    for i in range(len(list)):
        if list[i] == var:
            index.append(i+1)
            count += 1
    print(f"Your variable appears {count} times in the list.")
    print(f"The index of your variables in the  list is {index}.")


listsize = int(input("List size:"))
listainput = [input(f"Input {a+1}:") for a in range(listsize)]
variable = input("What is your variable?:")

funca(variable,listainput)

#exercicio 3

def power(a,b):
    elevado = b * ( a ** b )
    return print( a** elevado )

power(2,4)

#exercicio 4
import math


def calc(a):
    return print(f"Quadrado:{a**2}, Raiz:{math.sqrt(a)}, Len:{len(str(a))}")

calc(int(input("Input:")))

