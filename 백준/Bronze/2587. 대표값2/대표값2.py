import statistics
import sys
ls = []
for i in range(5):
    a = int(sys.stdin.readline())
    ls.append(a)
print(int(sum(ls)/5))
print(statistics.median(ls))