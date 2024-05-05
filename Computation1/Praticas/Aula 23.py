#exercicio 1

stringinput = input("Input numbers with commas separated:")
splitmatrix10 = []
splitmatrix = []

split = stringinput.split(",")

for i in range(len(split)):
    y = float(split[i])
    x = float(split[i]) + 10
    splitmatrix10.append(x)
    splitmatrix.append(y)

print(splitmatrix)
print(splitmatrix10)

#exercicio 2

inputname = input("Input the name of the people for the list separated by spaces:")
listname = inputname.split(" ")
bigfont = []
smallfont = []

for i in listname:
    if len(i) > 5:
        bigfont.append(i)
    else:
        smallfont.append(i)

print(f"Small names: {smallfont}, Big names: {bigfont}.")


#exercicio 3
import math
def week12(a,b):
    c = 0
    if b == True:
        for i in range(int(a+1)):
             c += i
    elif b == False:
        c = math.factorial(int(a))

    return c