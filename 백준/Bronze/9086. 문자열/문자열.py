import sys
x = int(input())
for i in range(x):
    s = str(sys.stdin.readline())
    a = s[0]
    b = s[-2]
    print("{}{}".format(a,b))