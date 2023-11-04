#exercicio 3

inputinvi = input("How many amigos:")
listnames = []
listnamesa = []
itera = 0

while itera < int(inputinvi):
    itera += 1
    name = (input(f"Name {itera}:")).lower()
    listnames.append(name)

print(f"A lista de convidados é: {listnames}")

for a1 in listnames:
    if a1[0] == "a":
        listnamesa.append(a1)

print(listnamesa)