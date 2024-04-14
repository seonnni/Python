# 1620
import sys
input = sys.stdin.readline
n, m = map(int, input().split()) 

pokedic_int_key = {}
pokedic_name_key = {}

for i in range(n):
    name = input().strip()
    pokedic_int_key[i] = name
    pokedic_name_key[name] = i

for _ in range(m):
    item = input().strip()
    if item.isdigit()== True: #입력값 숫자
        print(pokedic_int_key[int(item)-1])
    else: #입력값 문자
        print(pokedic_name_key[item]+1)