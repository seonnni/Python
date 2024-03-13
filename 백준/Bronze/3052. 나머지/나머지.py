divide = []
for i in range(10):
    divide.append(i)
    a = int(input())
    divide[i] = a

answer = []
for i in range(10):
    b = divide[i] % 42
    answer.append(b)
    
result = []
for value in answer:
    if value not in result:
        result.append(value)
    
print(len(result))    