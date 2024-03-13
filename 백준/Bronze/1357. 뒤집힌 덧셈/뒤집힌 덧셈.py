def Rev(num):
    num = str(num)
    num_rv = num[::-1]
    return num_rv
          
x, y = map(int, input().split())
rev_x = Rev(x)
rev_y = Rev(y)
hap = int(rev_x) + int(rev_y)
print(int(Rev(hap)))