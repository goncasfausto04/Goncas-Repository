#exercicio 1

matrix = [[1,2,3,],[4,5,6],[7,8,9]]
counter = 0
sumzito = 0
sumzao = 0


for i in matrix:
    for ite in i:
        sumzito += ite
        counter += 1
    sumzao += sumzito

print(sumzao)