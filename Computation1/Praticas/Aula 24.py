import sys

#exercicio 1
def greet(a):
    return print(f"Hello {a}.")

#exercicio 2
def areac(rad):
    area = 3.14 * rad**2
    return area

#exercicio 3
def numfinder(num,list):
    for i in list:
        if i == num:
            print("We Found it!")
            sys.exit()
    print("Number not found.")

#exercicio 4
def listeven(list):
    leven = []
    for i in list:
        if i % 2 == 0:
            leven.append(i)
    return leven