# 28278
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
dq = deque()

for _ in range(N):
    command = list(input().split())
    if command[0] == '1':
        dq.append(command[1])
    elif command[0] == '2':
        if len(dq) > 0 :
            tmp = dq.pop()
            print(tmp)
        else : print(-1)
    elif command[0] == '3':
        print(len(dq))
    elif command[0] == '4':
        if len(dq) > 0 :
            print(0)
        else:
            print(1)
    elif command[0] == '5':
        if len(dq) > 0:
            print(dq[-1])    
        else: print(-1)