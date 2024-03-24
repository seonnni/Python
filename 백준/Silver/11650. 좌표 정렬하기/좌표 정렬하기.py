# 11650
N = int(input())
ls = []
for i in range(N):
    x = list(map(int, input().split()))
    ls.append(x)
ls.sort()
for i in range(N):
    print(ls[i][0],ls[i][1])