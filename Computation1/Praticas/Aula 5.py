#exercicio 1

print("exercicio 1:")

string1 = "I am Learning about strings"

print(len(string1))

print(string1[5:13])
print(string1[-22:13])

#exercicio 2

print("exercicio 2:")

string2 ="I like oranges "
print((len(string2)))

replace = string2.replace("oranges", "apples")

print(replace)
print(replace*15)

#exercicio 3

print("exercicio 3:")

string3 = "patient"

tamanho = len(string3)
print(string3[tamanho//2])

#exercicio 4

print("exercicio 4:")

pycharm = "Pycharm is great!"
print(pycharm.replace(" ", "", 2))

#exercicio 5

print("exercicio 5:")

titanic = "Titanic is a sad film"
print(titanic.replace(" sad", ""))

#exercicio 6

print("exercicio 6:")
gert = "Gertrude bought 3 sodas for 1.20€ each."
print("len of gert:", len(gert))
preço = float(gert[-11:-7])

print("preço:", preço*int(gert[16]), "€")
