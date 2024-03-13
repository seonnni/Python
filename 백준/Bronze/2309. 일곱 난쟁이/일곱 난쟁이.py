ls = [int(input()) for _ in range(9)]
ls.sort()
sum_n = sum(ls)
# 모두 다 더하고 2명 뺐을 때, 그 값이 100
for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        if sum_n -ls[i]-ls[j] == 100:
            for k in range(len(ls)):
                if k == i or k == j:
                    pass
                else:
                    print(ls[k])
            exit()