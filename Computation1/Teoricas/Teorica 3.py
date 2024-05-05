valor = 0
x_sum = 0

while valor < 3:  # Change to loop 3 times
    x = float(input("Escreve um valor: "))
    x_sum = x_sum + x  # Calculate the sum of values
    valor = valor + 1

average = x_sum / 3  # Calculate the average after the loop

print("Average:", average)
