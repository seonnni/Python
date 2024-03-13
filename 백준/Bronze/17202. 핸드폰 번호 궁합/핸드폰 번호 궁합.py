import itertools as it
a = input()
b = input()
hap = list(it.chain(*zip(a,b)))


while len(hap) != 2:
    temp = []
    for i in range(len(hap)-1):
        a = (int(hap[i])+int(hap[i+1])) % 10
        temp.append(a)
    hap = temp

result = ''.join(map(str, hap))
print(result)