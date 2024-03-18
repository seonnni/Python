# 10773
ls = []
K = int(input())
for i in range(1,K+1):
    num = int(input())
    if num == 0:
        ls.pop()
    else:
        ls.append(num)
print(sum(ls))