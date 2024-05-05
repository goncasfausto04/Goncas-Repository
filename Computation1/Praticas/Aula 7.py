#exercicio 1

print("Useless Pergunta de Filmes:")

filmefav =  input("Qual é o teu filme favorito?")

print(f"O teu filme favorito é {filmefav}")

#exercicio 2

print("Repetir a palavra x vezes:")

word = input("Dá me uma palavra str:")
number = int(input("Agora dá me um número int:"))

print(number*word)

#exercicio 3

print("Calculadora por extenso:")

expressao = eval(input("Escreve uma expressão matemática:"))
print(expressao)

#exercicio 4

print("Calculadora de Segundos:")

horas = int(input("Dá me o número de horas:"))
minutos = int(input("Dá me o número de minutos:"))

print((horas*3600)+(minutos*60))

#exercicio 5

frase = input("Dá me uma frase pfv:")
numero = int(input("Agora um número:"))

print(frase[numero])

# exercicio 6

num = int(input("Dá me um número:"))

if num > 0:
    print("Número Positivo")
elif num < 0:
    print("Número Negativo")

if ((num % 2) == 0):
    print("Número Par")
elif ((num % 2) != 0):
    print("Número ìmpar")

if ((num % 3) == 0):
    print("É divisivel por 3!")
elif ((num % 3) != 0):
    print("Não é divisivel por 3!")

if ((num % 5) == 0):
    print("É divisivel por 5!")
elif((num % 5) != 0):
    print("Não é divisivel por 5!")

if (num <= 10) and (num >= -10):
    print("Está no intervalo de [-10 ; 10]!")
else:
    print("Não está no intervalo de [-10 ; 10]!")

#outra alternativa

numo = int(input("Dá me um número:"))

print("O numero é Par:", numo % 2 ==0)
print("O número é positivo:", numo > 0)
print("O número é negativo", numo < 0)
print("O número é divisivel por 3:", numo % 3 == 0)
print("O número é divisivel por 5:", numo % 5 == 0)
print("Está contido em [-10 , 10]:", numo >= -10 and numo <= 10)