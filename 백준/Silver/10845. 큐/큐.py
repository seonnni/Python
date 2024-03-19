# 10845
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
        if len(dq) > 0 :
            tmp = dq.popleft()
            print(tmp)
        else : print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) > 0 :
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(dq)>0:
            print(dq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(dq)>0:
            print(dq[-1])
        else:
            print(-1)