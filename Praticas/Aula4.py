#exercicio 1

w = float(2)
h = float(2.5)

area = w*h
perimetro = (2*w)+(2*h)

print("area:", area)
print("perimetro:", perimetro)

#exercicio 2

import math

c1 = float(3)
c2 = float(6)
h = math.sqrt((c1**2)+(c2**2))

print("hipotenusa:", h)

#exercicio 3

Tru = True
Fal = False

print("T and T:", Tru and Tru)
print("T and F:", Tru and Fal)
print("F and T:", Fal and Tru)
print("F and F:", Fal and Fal)

print("T or T:", Tru or Tru)
print("T or F:", Tru or Fal)
print("F or T:", Fal or Tru)
print("F or F:", Fal or Fal)
