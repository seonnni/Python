# 18258
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
dq = deque()

for _ in range(N):
    command = list(input().split())
    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'pop':
        if dq :
            print(dq[0])
            dq.popleft()
        else: print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) > 0 :
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(dq) > 0:
            print(dq[0])    
        else: print(-1)
    elif command[0] == 'back':
        if len(dq) > 0:
            print(dq[len(dq)-1])    
        else: print(-1)