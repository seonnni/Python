# 1247
import sys
input = sys.stdin.readline

for i in range(3):
    n = int(input())
    ls = []
    for j in range(n):
        ls.append(int(input()))
        
    if sum(ls) > 0:
        print('+')
    elif sum(ls) < 0:
        print('-')
    else:
        print('0')