import numpy as np

M = int(input("Write the number of lines: "))
N = int(input("Write the number of columns: "))
MAT = []
for i in range(0,M):
  temp = []
  for j in range(0,N):
   temp.append(float(input(f"Write the element ({i}, {j}): ")))
  MAT.append(temp)

print(np.array(MAT))
