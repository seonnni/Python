X = int(input())
N = int(input())
sum = 0
for i in range(N):
    a,b = map(int, input().split())
    c = a*b
    sum = sum + c

    
if sum == X :
    print("Yes")
else:
    print("No")