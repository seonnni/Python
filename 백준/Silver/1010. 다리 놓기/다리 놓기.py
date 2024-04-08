# 1010
import math
import sys
T = int(input())
for i in range(T):
    n,m = map(int, sys.stdin.readline().split())
    print(math.comb(m,n))