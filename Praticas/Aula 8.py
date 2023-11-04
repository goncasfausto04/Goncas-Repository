#exercicio 1

pine = "Pineapple CANNOT be on  pizza,  ever!"

print(pine.replace("  ", " "))

#exercicio 2

first = input("Insert the First half:")
second = input("Insert the Second half:")

print(first + ", " + second)

#exercicio 3

color = "red, white, black, green, orange, purple"

colori = input("Tell me your favorite color:")

print("Your color is good:", colori.lower() in color )

#exercicio 4

month_names = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'}

date = input("Tell me todays date in the DD/MM/YYYY format please!")
day = date[0:2]
month = date[3:5]
year =date[6:10]

print(f"Today is the {day},of {month_names[month]},of {year}")

#exercicio 5

num1 = float(input("Give me any number:"))
num2 = float(input("Give me another number:"))
operation = input("Write what you want to do with them (+, -, *, **, /, //):")

print("The result of the operation is:")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "//":
    print(num1 // num2)
elif operation == "**":
    print(num1 ** num2)
