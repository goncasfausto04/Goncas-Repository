#exercio 1

int1 = input("Insert an int number:")
int2 = int(int1)

if int2 < 1000:
    print("your number is small")
elif int2 > 999:
    print(f"Your number has {len(int1)} digits")

#exercicio 2

code = input("Input your country phone code with a +:")

codeDic = { "+351" : "Portugal" ,
          "+90" : "Turkey" ,
          "+364" : "Iceland" }

if code in codeDic:
    print(f"Your country is {codeDic[code]}")
else:
    print("Country not real.")

#exercico 3

nome = input("What is your name?")
nomea = nome[:-1] + "inha"
nomeo = nome[:-1] + "inho"

if nome[-1] == "a":
    print(nomea)
elif nome[-1] == "o":
    print(nomeo)
else:
    print(f"O teu nome ({nome}) não é nada de especial!")

#exercicio 4

nova = input("Tell me something about NOVA:")
novalower = nova.lower()

if "nova" in novalower:
    print(novalower.replace("nova", "Universidade Nova de Lisboa"))
else:
    print("Are you sure you are talking about NOVA?")

#exercicio 5

pet = input("Input 1 if your pet is a Dog, 2 if it is a Cat and 3 if its any other option:")

cost = { "1":"40",
         "2":"50" ,
         "3":"60"}

taxa = float(cost[pet]) + 0.23*float(cost[pet])

print("Sem IVA:" + cost[pet], "I" ,"Com IVA:" , taxa )