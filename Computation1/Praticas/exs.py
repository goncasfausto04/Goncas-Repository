def f1(M):
    x = 0
    for i in M:
        x = x  + f2(i)
        return x

def f2(L):
    x = L[0]
    for i in range (1, len(L)):
        if L[i] > x:
            x = L[i]
    return x

k = [[4,3,2,1],[8,5,1,4]]
print(f1(k))

for i in k:
    print(i)
print(False or False)