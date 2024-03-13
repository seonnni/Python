submit = []  
for i in range(28):
    submit.append(i)
    submit[i] = int(input())
    
not_submit = []
for i in range(1,31):
    if i not in submit:
        not_submit.append(i)
print(min(not_submit))
print(max(not_submit))