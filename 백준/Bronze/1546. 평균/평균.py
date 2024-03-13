n = int(input())

score = map(int, input().split())
s_list = list(score)
score_max = max(s_list)

new_score = []
for i in range(n):
    a = s_list[i]/score_max*100
    new_score.append(a)
hap = 0
for i in range(n):
    hap += new_score[i]
print(hap/n)