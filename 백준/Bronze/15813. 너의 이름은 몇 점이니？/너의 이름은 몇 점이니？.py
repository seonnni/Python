n = int(input())
name = input()

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

hap = 0
for i in range(n):
    a = alpha.index(name[i]) + 1
    hap += a
    
print(hap)