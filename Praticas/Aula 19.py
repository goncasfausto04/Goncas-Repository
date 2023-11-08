#exercicio 1

people = int(input("How many people are working on your department?"))

salaries = [int(input(f"Salary {i+1}:")) for i in range(people)]

newsalaries = [i+500 for i in salaries]

print(newsalaries)
