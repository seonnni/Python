# 2161
N = int(input())
ls = []
ans = []

for i in range(1,N+1):
    ls.append(i)

while (len(ls) != 0):
    ans.append(ls.pop(0))
    if(len(ls) != 0):
        ls.append(ls.pop(0))

for j in ans:
    print(j, end=" ")