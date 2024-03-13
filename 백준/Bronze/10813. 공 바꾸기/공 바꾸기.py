n, m  = map(int, input().split())
ball = []
for i in range(n):
    ball.append(i+1)
for _ in range(m):
    i, j= map(int, input().split())
    a = ball[i-1]
    ball[i-1] = ball[j-1]
    ball[j-1] = a
    
print(*ball)