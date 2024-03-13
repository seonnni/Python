import sys
N = int(sys.stdin.readline()) 
ls = [int(sys.stdin.readline()) for _ in range(N)]
ls.sort(reverse=True)
for i in ls:
    print(i)