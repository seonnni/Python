import sys    
C = int(sys.stdin.readline())
li = []
for i in range(C):
    li = list(map(int,sys.stdin.readline().split()))
    
    sum = 0
    avg = 0
    count = 0
    for j in range(1, len(li)):
        sum += li[j]
    avg = sum / li[0]

    for k in range(1, len(li)):
        if li[k] > avg:
            count += 1
    result = round(count*100 / li[0],3)
    print(f'{result:.3f}%')
    li.clear()