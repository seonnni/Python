# 2576
ls = []
for i in range(7):
    ls.append(int(input()))
hol = []
for i in ls:
    if i % 2 != 0:
        hol.append(i)
        
if len(hol) == 0:
    print(-1)
else:
    print(sum(hol))
    print(min(hol))