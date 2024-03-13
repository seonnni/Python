k = int(input())
a = 1
b = 0
for i in range(1,k+1):
    a_r = a
    a = b
    b = a_r + a
print(a, b)