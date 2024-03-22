# 10867
N = int(input())
ls = list(map(int, input().split()))
ls = list(set(ls)) # set은 중복을 허용하지 않음
ls.sort()

for i in ls:
    print(i, end=' ')