import sys
N = int(input())
for i in range(N):
    a = sys.stdin.readline()
    a = a[0].upper()+a[1:]
    print(a,end='')