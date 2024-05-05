#exercicio 1

list1 = [2, 7, 2, 5, 4]

for i in range(len(list1)):
    if i % 2 == 0:
        print(list1[i] * 3)
    else:
        print(list1[i] * 2)

#exercicio 2

my_list = [3, 5, 7, 9]

my_list[0] = 100
count = 0
for i in my_list:
    if i > 6:
        count += i

print(f"The sum of the elements > 6 is: {count}")

#exercicio 3

inputitemq = input("How many items are you going to buy?:")
counter = 0
item = []

while counter < int(inputitemq):
    counter += 1
    item.append(input("Item:"))


print(f"This is your list: {item}")


# exercicio 4

input_count = int(input("How many numbers do you want to enter? "))
countern = 0
even_count = 0
odd_count = 0

while countern < input_count:
    number = int(input(f"Enter number {countern + 1}: "))
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    countern += 1

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
