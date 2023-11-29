#exercicio 4

def primecalc(num):
    if num < 2:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True


def nprimenumbers(num):
    primelist = []
    for i in range(num+1):
        if primecalc(i) == True:
            primelist.append(i)
    return primelist

print(nprimenumbers(9))