# 10814
N = int(input())
user = []
for _ in range(N):
    age, name = map(str, input().split())
    user.append([int(age),name])

user = sorted(user, key=lambda x: x[0])

for i in user:
    print(*i)