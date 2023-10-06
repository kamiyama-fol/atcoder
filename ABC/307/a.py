n = int(input())
a =list(map(int, input().split(" ")))
week = 0
for j in range(n):
    answer[j]=0
for i in range(n):
    answer[week] =answer[week] + a[i]
    if i % 6 ==0:
        week = week + 1