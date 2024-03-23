# 17206
T = int(input())
N = list(map(int, input().split()))
ls = [0] * 80001
ans = 0

for i in range(80001):
    if i % 3 == 0 or i % 7 == 0:
        ans += i
    ls[i] = ans
for j in N:
    print(ls[j])  