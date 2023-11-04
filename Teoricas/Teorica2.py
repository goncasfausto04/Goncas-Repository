# for itera todos os valores da lista ou str

x = "Boas"

for i in x:
    print(i)
    print("---")

# range sequência [v1,v2[ , conta os valores

N = int(input("número pfv:"))

for coisa in range(N):
    print("hello")

#

for num in range(5):
    print(num)

#escrever a palavra input ao contrário

my_string = input("escreve aqui:")
t = ""
for iter in range(len(my_string) - 1, -1, -1):
    t = t + my_string[iter]

print(t)