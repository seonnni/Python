right = [1, 1, 2, 2, 2, 8]
dong = list(input().split())
answer = []
for i in range(6):
    if int(right[i]) - int(dong[i])> 0:
        answer.append(int(right[i]) - int(dong[i]))
    elif int(right[i]) - int(dong[i]) < 0:
        answer.append(int(right[i]) - int(dong[i]))
    else :
        answer.append(0)
print(*answer)