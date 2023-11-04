#exercio 1 ppw funções
def sum(N):
    resultado = 0
    for i in range(1, N+1):
        resultado += i
    return (resultado)



while True:
    N = int(input("Write a Positive input:"))
    if N > 0:
        break
    else:
        print("Try again!")


print(f"The sommatory of all numbers leading to {N} is {sum(N)}")

#exercicio 2 ppw funções

def print_letters( s : str, i : int, j : int ):
    print(s[i], s[j])


    s = input("Write a str:")
    i = int(input("i:"))
    j = int(input("j:"))

    if i > len(s) - 1 or j > len(s) - 1:
        print("Bué gay erraste.")
