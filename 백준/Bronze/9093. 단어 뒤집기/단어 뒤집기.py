import sys  
T = int(input())

for i in range(T):
    result = []
    test = sys.stdin.readline().split()
    for j in range(len(test)):
        word = test[j]
        result.append(word[::-1])
    print(' '.join(result))