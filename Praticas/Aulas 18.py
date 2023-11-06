#exercicio 1

matrix = [[1,2,3,],[4,5,6],[7,8,9]]
counter = 0
counterd = 0
listd = []
sumzito = 0
sumzao = 0


for i in matrix:
    for ite in i:
        sumzito += ite
        counter += 1
    sumzao += sumzito

print(sumzao)
print(matrix[2])

for i in matrix:
    listd.append(i[counterd])
    counterd += 1

print(listd)

#exercicio 2

sizelist = int(input("How many items?:"))

list1 = [int(input("Input:")) for i in range(sizelist)]

option = input("1, 2 or 3?:")

if option == "1":
    list2 = [i**2 for i in list1]
    print(f"The list squared is: {list2}")
elif option == "2":
    matrixfim = []
    matrixfim.append(list1)
    listdouble = [i * 2 for i in list1]
    matrixfim.append(listdouble)
    listtriple = [i * 3 for i in list1]
    matrixfim.append(listtriple)
    print(matrixfim)
elif option == "3":
    sizelist2 = int(input("How many items?:"))

    list2 = [int(input("Input:")) for i in range(sizelist2)]
    matrix3 = []
    matrix3.append(list1)
    matrix3.append(list2)
    print(matrix3)
else:
    print("Wrong input.")