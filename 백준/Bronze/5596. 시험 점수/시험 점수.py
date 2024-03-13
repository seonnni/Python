minkook = list(map(int, input().split()))
manse = list(map(int, input().split()))
S = sum(minkook)
T = sum(manse)
if S > T:
    print(S)
elif S < T:
    print(T)
else:
    print(S)