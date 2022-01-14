import math
import numpy as np
import matplotlib.pyplot as plt
n = 1
p = 40
m = 5
matrix = np.zeros((p,m))
for i in range(0,p,1):
    for j in range(0,m,1):
        matrix[i][j] = n
        n = n + 2

prime = []
prime.append(2)
prime.append(3)
prime.append(5)

for i in range(0,p,1):
    for j in range(0,m,1):
        num = int(matrix[i][j])
        if num % 3 !=0 and num % 11 !=0 and  num % 5 !=0 and  num % 7 !=0 and  not int(math.sqrt(num)+0.5)**2 == num and num!=1:
            prime.append(num)
print(matrix)
print(prime)
k = 0

x = prime
y = []

for i in prime:
    y.append(math.sin(i))

plt.plot(x,y,'c-',markersize = 3)
plt.show()
