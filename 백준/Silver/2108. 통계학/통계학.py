# 2108
import sys
import statistics as st
N = int(sys.stdin.readline())
ls = []
for i in range(N):
    ls.append(int(sys.stdin.readline()))
    
print(round(st.mean(ls)))
print(st.median(ls))
a = st.multimode(ls)
a.sort()
m = a[1] if len(a) > 1 else a[0]
print(m)
print(max(ls)-min(ls))