a,b = map(int, input().split())
ls = []
for i in range(1,b+1):
    for j in range(i):
        ls.append(i) 
hap = []
for i in range(a-1,b):
    a = ls[i]
    hap.append(a)
    
hap_list = sum(hap)
print(hap_list)