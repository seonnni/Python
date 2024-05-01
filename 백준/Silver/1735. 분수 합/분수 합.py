# 1735
import math
a, b = map(int, input().split())
c, d = map(int, input().split())

bunja = a*d + b*c
bunmo = b*d

my = math.gcd(bunja, bunmo)
bunja //= my
bunmo //= my

print(bunja, bunmo)