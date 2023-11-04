#exercicio 1

my_list = [1,2,3]
total = 0

for i in my_list:
    total += i

avg = total/len(my_list)

while avg <= 5.0:
    add = int(input("Add new nmr:"))
    my_list.append(add)
    avg = (total+add)/len(my_list)
    if avg <= 5:
        print(f"Your average needs to be higher than 5 and it is {avg}")
    else:
        print(f"Your average is {avg}, that is higher than 5 as requested!")

#exercicio 2 e 3

randomint = 5
guess = float(input("Guess a number:"))
count = 0

while randomint != guess:
    count += 1
    print("Try again:")
    guess = float(input("Guess a number:"))

if count <= 2:
    print("You got it! Congrats!")
elif count >= 3 and count <= 5:
    print(f"You got it, but not that impressive, since it took you {count + 1} tries.")
elif count > 5:
    print(f"Really! {count + 1} tries? Zero luck for you!")

#exercicio 4

stringinput = input("Input a string please:")
capletters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
countcap = 0

for i in stringinput:
    if i in capletters:
        countcap += 1

if countcap >= 1:
    print("Capitall leters detected.")
else:
    print("No capital letters detected.")

#exercicio 5

# Given encrypted message
message = 'blephatxyzrs gotwo_na hatxyzgo'

# Decrypt the message
message = message.replace('xyz', 'e')
message = message.removeprefix('blep')
message = message.removesuffix('go')
message = message.replace('two_n', 'nn')

print(message)
