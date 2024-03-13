a = int(input())
b = int(input())
c = int(input())

result = a * b * c
result_l = list(map(int, str(result)))
for i in range(10):
    print(result_l.count(i))
