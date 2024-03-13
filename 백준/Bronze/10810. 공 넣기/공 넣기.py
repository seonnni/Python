n, m  = map(int, input().split())
ball = []
for i in range(n):
    ball.append(0)

for _ in range(m):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        ball[n-1] = k

for i in ball:
    print(i, end=' ')