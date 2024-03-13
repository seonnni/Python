a, b, c = map(int, input().split())
list = [a,b,c]
k = max(list)
list.remove(k)
print(max(list))