#exercicio 1

people = int(input("How many people are working on your department?"))

salaries = [int(input(f"Salary {i+1}:")) for i in range(people)]

newsalaries = [i+500 for i in salaries]

print(newsalaries)

#exercicio 2

givenmatrix = [[5,4],[3,5],[1,2],[0,0]]
row = 0
column = 0
bigger3 = 0

print(givenmatrix[1][0])
print(givenmatrix[2][1])

print(f"The sum of numbers in the corner is:{givenmatrix[0][0] + givenmatrix[3][1] + givenmatrix[0][1] + givenmatrix[3][0]}")

for i in givenmatrix:
    row += 1
for i in givenmatrix[0]:
    column += 1

print(f"Rows:{row}")
print(f"Columns:{column}")

for i in givenmatrix:
    for ite in i:
        if ite > 3:
            bigger3 += 1

print(f"There are {bigger3} numbers bigger than 3.")

#exercicio 3

rowsmatrix = int(input("How many rows you want in your matrix?:"))
colummatrix = int(input("How many columns you want your matrix to have?:"))
matrix1 = []

for i in range(rowsmatrix):
    fila = []
    for i in range(colummatrix):
        input1 = input("Input:")
        fila.append(input1)
    matrix1.append(fila)

print(matrix1)

#or

# Ask the user for the number of rows and columns
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))

# Create the matrix using a nested list comprehension
matrixcoiso = [[int(input(f"Enter element at row {i + 1}, column {j + 1}: ")) for j in range(num_cols)] for i in range(num_rows)]

print(matrixcoiso)
