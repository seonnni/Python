a,b = map(str, input().split())
a_ls = []
b_ls = []
for i in range(2,-1,-1):
    a_ls.append(a[i])
    b_ls.append(b[i])
a = int(''.join(a_ls))
b = int(''.join(b_ls))

if a > b:
    print(a)
else:
    print(b)