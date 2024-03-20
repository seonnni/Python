# 15688
import sys
N = int(sys.stdin.readline())
ls = []
for i in range(N):
    ls.append(int(sys.stdin.readline()))
for i in sorted(ls):
    print(i)