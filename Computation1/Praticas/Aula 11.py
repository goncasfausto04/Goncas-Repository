#exercicio 1

list1 = list(range(1,11))

for i in list1:
    print(i)

#exercicio 2

list2 = list(range(1, 101))

for i in list2:
    if i % 3 == 0:
        print(i)

#exercicio 3

list2 = list(range(1, 101))

for it in list2:
    if it % 2 != 0:
        print(it)

#exercicio 4

list2 = list(range(1, 101))

for ite in list2:
    if ite % 10 != 0:
        print(ite)
    elif ite % 10 == 0:
        print(ite, "You have printed 10 numbers!")

#exercicio 5

input1 = input("Tell me one word:")

for iter in input1:
    if iter == "a":
        print("I found one a!")

#exercicio 6

input2 = input("Tell me another word:").lower()
input3 = input("Now tell me a letter:").lower()

count = input2.count(input3)

print(f"You have {count} times {input3} in {input2} ")