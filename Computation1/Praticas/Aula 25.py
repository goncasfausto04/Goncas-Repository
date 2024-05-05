#exercicio 1

def vowelremover(string):
    vowel = ["a", "e","i","o","u","A","E","I","O","U"]
    novowelstringl = []
    for i in string:
        if i not in vowel:
            novowelstringl.append(i)
    novowelstring = "".join(novowelstringl)
    return novowelstring

def vowelrereverse(string):
    return vowelremover(string)[::-1]

#exercicio 2
def matrixavg(matrix):
    total = 0
    count = 0
    for line in matrix:
        for element in line:
            total += element
            count += 1
    avg = total/count
    return avg

def maxvalue(matrix):
    matrixline = []
    for line in matrix:
        for element in line:
            matrixline.append(element)
    return max(matrixline)

#exercicio 3

def primecalc(num):
    if num < 2:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

#exercicio 4

def nprimenumbers(num):
    primelist = []
    for i in range(num+1):
        if primecalc(i) == True:
            primelist.append(i)
    return primelist