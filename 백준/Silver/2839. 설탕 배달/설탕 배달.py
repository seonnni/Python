n = int(input())

if n % 5 == 0:
    print(n//5)
else:
    p = 0
    while n > 0:
        n -=3
        p += 1
        if n % 5== 0: # 3과 5를 조합해서 담을 수 있을 때
            p += n//5
            print(p)
            break
        elif n ==1 or n == 2: # 나눌 수 없을 때
            print(-1)
            break
        elif n == 0 : # 3으로 나누어 떨어질 때
            print(p)
            break