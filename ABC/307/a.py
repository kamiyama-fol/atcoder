n = int(input())
a =list(map(int, input().split(" ")))
week = 0
answer=[]
for j in range(n):
    answer.append(0)
for i in range(n*7):
    answer[week] =answer[week] + a[i]
    if i % 6 ==0:
        week = week + 1
print(answer)