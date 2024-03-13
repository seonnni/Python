num = int(input())
re_num = num
t = 0
while True:
    a = num // 10
    b = num % 10
    c = a + b
    d = str(b) + str(c%10)
    num = int(d)
    t += 1

    if (re_num == num):
      print(t)
      break