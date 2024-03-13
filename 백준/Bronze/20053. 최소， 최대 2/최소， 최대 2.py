T = int(input())
for i in range(T):
    N = int(input())
    ls = list(map(int, input().split()))
    print(min(ls),max(ls))