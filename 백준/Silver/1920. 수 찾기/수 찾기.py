N = int(input())
first_ls = set(map(int, input().split()))

M = int(input())
second_ls = list(map(int, input().split()))

for i in range(M):
    if second_ls[i] in first_ls:
        print(1)
    else:
        print(0)