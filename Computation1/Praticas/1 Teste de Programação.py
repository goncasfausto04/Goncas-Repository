#Group1

#1.B 2.AB 3.D 4.A 5.A 6.D 7.C 8.G

#Group 2

#1.
#a)3
#b)"Pineapple on pizza is allowed"
#"Pineapple on pizza is allowed"
#"Pineapple on pizza is allowed"

#2.
# elif door[0] == 8 or door[0:1] == 10:
#if name.lower() == "judy" ... :

#3.
#range
#range(1.17)

#4.You have to input a number, if you on the second input 1 or 2m it prints "You silly goose"
#if you input 1 or 2  it creates a list with the numbers 10 and 20 and with this it will use a for loop
#and add 1 to either of your choices so they are included in the range and it will multiply your number
#10 or 20 times creating the "tabuada"



name = input("Your name:")
number = input("You student number:")
nclasses = int(input("Your number of classes:"))
count = 0
count1 = 0
count2 = 0
count3 = 0
tot = 0
listclass = []
listclassPrice = []

while count < nclasses:
    count += 1
    classcode = input(f"Class code {count}:")
    listclass.append(classcode)

for ite in listclass:
    if ite[-3:] == "III":
        listclassPrice.append(150)
        count3 += 1
    elif ite[-2:] == "II":
        listclassPrice.append(120)
        count2 += 1
    else:
        listclassPrice.append((100))
        count1 += 1

scholarships =["20221111", "20222222", "20223333", "20224444", "20219999", "20218888", "2021444"]

if number in scholarships:
    for conti in listclassPrice:
        tot += conti
    total = tot * 0.85
else:
    for cont in listclassPrice:
        tot += cont
    total = tot

#Receipt
print("Here is your receipt:")
print(f"Name: {name}")
print(f"Year 1 classes: {count1}")
print(f"Year 2 classes: {count2}")
print(f"Year 3 classes: {count3}")
print(f"Final tuiton {total}")