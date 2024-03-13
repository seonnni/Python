import statistics
import sys
ls = []
for i in range(10):
    a = int(sys.stdin.readline())
    ls.append(a)   
print(int(sum(ls)/10)) 
print(statistics.mode(ls))