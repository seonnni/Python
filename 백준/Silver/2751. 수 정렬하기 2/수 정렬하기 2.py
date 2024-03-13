import sys
N = int(input())
li = []
for i in range(N):
    a = int(sys.stdin.readline())
    li.append(a)
li.sort()
for i in range(N):
    print(li[i]) 