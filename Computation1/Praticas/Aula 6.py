#exercicio 1

my_string = "Gertrude went to buy groceries"

a = my_string[16:21]
b = my_string[1]
c = my_string[0:14]

print(a)
print(b)
print(c)

#exercicio 2

word = "nova"
word_capital = "NOVA"

unl = "Universidade NOVA de Lisboa"

print("nova em NOVA:", word in unl)
print("Nova em NOVA:", word_capital in unl)

#exercio 3

import math

my_string = "My circle has a radius of 3, and my square has a length of 4.5."
r = float(my_string[26])

Circ = 2*(math.pi)*r
Area = (math.pi)*(r**2)

print("Perimetro:", Circ)
print("Area:", Area)

#exercicio 4

one = "18"
two = "44"
three = "22"

print(one+two)
print(three*2)
print(int(two)+int(three))
print(int(three)-int(three[0]))

#exercicio 5

lista = ["A","B","C","D","E"]

print(lista[2])

lista[2] = "X"

print(lista[2])

lista2 = ["F", "G", "H"]

print(len(lista + lista2))
