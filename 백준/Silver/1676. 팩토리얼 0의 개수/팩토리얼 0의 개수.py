# 1676
import math
n = int(input())
t = 0
for i in str(math.factorial(n)) [::-1]:
    if i != '0':
        break
    else:
        t += 1
print(t)