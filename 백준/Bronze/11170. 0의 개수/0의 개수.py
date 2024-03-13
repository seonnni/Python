T = int(input())
            
for i in range(T):
    n, m = map(int, input().split())
    count = 0
    for j in range(n,m+1):
        w = str(j)
        count += w.count('0')
    print(count)