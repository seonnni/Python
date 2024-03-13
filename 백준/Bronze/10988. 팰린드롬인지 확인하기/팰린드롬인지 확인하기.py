word = input()

if all(word[i]==word[-i-1] for i in range(len(word)//2)):
    print(1)
else:
    print(0)