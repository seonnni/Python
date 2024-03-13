s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = [-1]*26

for i in s:
    alpha_list[alpha.index(i)] = s.index(i)
    
for i in alpha_list:
    print(i, end=' ')