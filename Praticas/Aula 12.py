#exercicio 1

input1 = (input("Input a word:")).lower()
vowel = ["a", "e", "i", "o", "u"]
countv = 0

for i in input1:
    if i not in vowel:
        countv += 1

print(countv)

#exercicio 2

inputclasses = float(input("Tell me the nº of classes held:"))
inputattend = float(input("Tell me the nº of classes attended:"))

attendance = (inputattend/inputclasses) *100

print(f"Your attendance is: {attendance} %")

if attendance >= 75:
    print("You will be allowed to take the exam.")
elif attendance < 75:
    inputcause = (input("Do you have a medical cause (Y or N):")).lower()
    if inputcause == "y":
        print("You will be able to do the exam!")
    elif inputcause == "n":
        print("You will not be able to take the exam!")

#exercicio 3

while True:
    grade1 = float(input("Input Grade1:"))
    if grade1 in range(0,21):
        break
    else:
        print("Try again!")

while True:
    grade2 = float(input("Input Grade2:"))
    if grade2 in range(0,21):
        break
    else:
        print("Try again:")

inputuser = input("Press 1 for average or 2 for greatest:")

if inputuser == "1":
    print("The average  is:",(grade1+grade2)/2)
elif inputuser == "2":
    if grade1>grade2:
        print(grade1)
    elif grade2>grade1:
        print(grade2)

#exercicio 4

inputdepart = input("What is your department:")
inputyear = input("How many years did you work on that department:")

if inputdepart.lower() == "managment" or inputdepart.lower() == "software":
    if float(inputyear) >= 3:
        print("Your Bonus is 30%")
    elif float(inputyear) < 3:
        print("Your Bonus is 25%")

elif inputdepart.lower() == "finance":
    if float(inputyear) >= 5:
        print("Your Bonus is 20%")
    elif float(inputyear) <5:
        print("Your Bonus is 15%")

elif inputdepart.lower() == "maintenence":
    print("Your Bonus is 10%")