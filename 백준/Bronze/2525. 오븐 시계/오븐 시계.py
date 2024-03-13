a, b = map(int, input().split())
c= int(input())
h= c//60
m= c%60
a= a+h
b= b+m
if b>=60:
    a = a+1
    b = b-60
    if a >= 24:
        a = a-24
        print(a,b)
    else:
        print(a,b)
else :
    if a>=24 :
        a = a-24
        print(a,b) 
    else :
        print(a,b) 