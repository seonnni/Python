# 1673
try:
    while True:
        n, k = map(int, input().split())
        chicken= n + (n//k)
        while n>=k:
            n = (n//k) + (n%k)
            chicken += n//k
        print(chicken)
except:
    exit()