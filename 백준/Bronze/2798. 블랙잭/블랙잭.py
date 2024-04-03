# 2798
N,M = map(int, input().split())
ls = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1,N):
            if ls[i] + ls[j] + ls[k] > M:
                continue
            else:
                result = max(result, ls[i] + ls[j] + ls[k])

print(result)