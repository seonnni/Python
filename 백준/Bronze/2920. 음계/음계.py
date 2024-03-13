pitch = '1 2 3 4 5 6 7 8'
pitch_rv = '8 7 6 5 4 3 2 1'
x = str(input())

if x == pitch:
    print("ascending")
elif x == pitch_rv:
    print("descending")
else:
    print("mixed")