# 1748
import sys
n = sys.stdin.readline().strip()
result = 0

if len(n) == 1:
    result = int(n)
else:
    result = 11
    for i in range(2, 10):
        if len(n) == i:
            result += i*(int(n)-10**(i-1))
            break
        else:
            result += i*(9*10**(i-1))+1
print(result)