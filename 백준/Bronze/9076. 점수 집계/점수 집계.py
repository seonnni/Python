T = int(input())
for i in range(T):
    score = list(map(int, input().split()))
    
    if max(score)- min(score) > 5 :
        print("KIN")
    else :
        score.remove(max(score))
        score.remove(min(score))
        print(sum(score))