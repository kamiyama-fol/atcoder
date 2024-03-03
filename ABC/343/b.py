n = int(input())
a = []
answer = []
for i in range(n):
    a.append(list(map(int, input().split(" "))))
    for j in range(n):
        if a[i][j] ==1:
            answer.append([])
            answer[i].append(str(j+1))
for l in answer:
    if l !=[]:
        print(" ".join(l))

