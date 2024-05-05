#exercicio 1

print("ex1:")

list1 = [-1, 3, 4, 5]
list2 = [-2, 3, 5, 6]

for i in list1:
    if i in list2:
        print(i, end=" ")

#exercicio 2
print("")
print("ex2:")

i = 0
list3 = []
list4 = []

while i<5:

    i += 1
    input1 = input(f"Int{i}:")
    list3.append(int(input1))

print(list3)


for val in range(len(list3)):
    if list3[val] > 10:
        print(val)
        list4.append(list3[val])

print(list4)

#exercicio 3
print("ex2:")

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